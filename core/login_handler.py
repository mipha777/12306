import time
from typing import Dict
from core.session_manager import SessionManager
from utils.captcha_tool import get_captcha_input

# 12306 登录相关 URL
CAPTCHA_URL = "https://kyfw.12306.cn/passport/captcha/captcha-image64"
CAPTCHA_CHECK_URL = "https://kyfw.12306.cn/passport/captcha/captcha-check"
LOGIN_URL = "https://kyfw.12306.cn/passport/web/login"
AUTH_UAMTK_URL = "https://kyfw.12306.cn/passport/web/auth/uamtk"
AUTH_CLIENT_URL = "https://kyfw.12306.cn/otn/uamauthclient"


class LoginHandler:
    def __init__(self, session_manager: SessionManager, username: str, password: str):
        self.sm = session_manager
        self.session = self.sm.get_session()
        self.username = username
        self.password = password

    def _get_captcha(self) -> str:
        """获取验证码并让用户输入"""
        params = {
            "login_site": "E",
            "module": "login",
            "rand": "sjrand",
            "M": str(int(time.time() * 1000))
        }
        try:
            resp = self.session.get(CAPTCHA_URL, params=params)
            resp.raise_for_status()
            captcha_data = resp.json()
            if captcha_data.get("result_code") == "0":
                print("验证码获取成功！")
                return get_captcha_input(captcha_data["image"])
            else:
                print(f"获取验证码失败: {captcha_data.get('result_message')}")
                return ""
        except Exception as e:
            print(f"请求验证码接口时出错: {e}")
            # 调试代码：打印服务器返回的原始内容
            if 'resp' in locals():
                print(f"服务器返回内容: {resp.text}")
            return ""

    def _check_captcha(self, captcha_input: str) -> bool:
        """校验验证码"""
        data = {
            "answer": captcha_input,
            "login_site": "E",
            "rand": "sjrand"
        }
        try:
            resp = self.session.post(CAPTCHA_CHECK_URL, data=data)
            resp.raise_for_status()
            result = resp.json()
            if result.get("result_code") == "4":
                print("验证码校验通过！")
                return True
            else:
                # 12306 返回的提示信息在 result_message 中，可能比较通用
                print(f"验证码校验失败: {result.get('result_message')}")
                return False
        except Exception as e:
            print(f"校验验证码接口时出错: {e}")
            return False

    def _perform_login(self, captcha_result: str) -> Dict:
        """执行登录请求"""
        login_data = {
            "username": self.username,
            "password": self.password,
            "appid": "otn"
        }
        try:
            resp = self.session.post(LOGIN_URL, data=login_data)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            print(f"登录请求失败: {e}")
            return {}

    def _auth_uamtk(self) -> str:
        """第一次认证，获取 uamtk"""
        try:
            resp = self.session.post(AUTH_UAMTK_URL, data={"appid": "otn"})
            resp.raise_for_status()
            result = resp.json()
            if result.get("result_code") == 0:
                print("第一步认证成功，获取 uamtk。")
                return result.get("newapptk")
            else:
                print(f"第一步认证失败: {result.get('result_message')}")
                return ""
        except Exception as e:
            print(f"请求 uamtk 认证时出错: {e}")
            return ""

    def _auth_client(self, uamtk: str) -> bool:
        """第二次认证，最终确认登录状态"""
        try:
            resp = self.session.post(AUTH_CLIENT_URL, data={"tk": uamtk})
            resp.raise_for_status()
            result = resp.json()
            if result.get("result_code") == 0:
                print("第二步认证成功，登录完成！")
                return True
            else:
                print(f"第二步认证失败: {result.get('result_message')}")
                return False
        except Exception as e:
            print(f"请求客户端认证时出错: {e}")
            return False

    def login(self) -> bool:
        """完整的登录流程"""
        # 0. 预先访问登录页，获取必要的 cookie
        try:
            self.session.get("https://kyfw.12306.cn/otn/resources/login.html", timeout=5)
        except Exception as e:
            print(f"W: 访问登录页失败，但这不影响主要流程: {e}")

        print("开始登录...")
        # 1. 获取并校验验证码
        captcha_input = self._get_captcha()
        if not captcha_input:
            return False

        if not self._check_captcha(captcha_input):
            return False

        # 2. 提交登录表单
        login_result = self._perform_login(captcha_input)
        if login_result.get("result_code") != 0:
            print(f"登录失败: {login_result.get('result_message', '未知错误')}")
            return False
        print("登录表单提交成功！")

        # 3. 双重认证
        uamtk = self._auth_uamtk()
        if not uamtk:
            return False

        if not self._auth_client(uamtk):
            return False

        # 4. 保存 cookie
        self.sm.save_cookies()
        return True

    def is_login(self) -> bool:
        """检查当前 session 是否处于登录状态"""
        # 简单的检查方法：尝试请求一个需要登录的接口
        # 这里以第二次认证接口为例，如果能拿到用户名，说明在线
        try:
            resp = self.session.post(AUTH_CLIENT_URL, data={"tk": ""}) # 传空 tk 必然失败，但可以检查 cookie
            if resp.status_code == 200 and "username" in resp.json():
                 print(f"✅ 用户 {resp.json()['username']} 当前已登录。")
                 return True
        except Exception:
            pass
        
        print("ℹ️ 当前未登录或登录已失效。")
        return False 