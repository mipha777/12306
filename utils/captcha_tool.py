import base64
from io import BytesIO
from PIL import Image
import webbrowser
import tempfile
import os

CAPTCHA_IMAGE_PATH = os.path.join(tempfile.gettempdir(), "captcha.jpg")


def get_captcha_input(image_base64: str) -> str:
    """
    解码 Base64 验证码图像，显示并获取用户输入。

    :param image_base64: Base64 编码的验证码图片字符串。
    :return: 用户输入的验证码坐标字符串，例如 "45,51,105,120"。
    """
    try:
        # 解码 Base64
        image_data = base64.b64decode(image_base64)
        image = Image.open(BytesIO(image_data))

        # 保存为临时文件并用默认程序打开
        image.save(CAPTCHA_IMAGE_PATH)
        print(f"ℹ️ 验证码图片已保存至：{CAPTCHA_IMAGE_PATH}")
        webbrowser.open(f"file://{os.path.realpath(CAPTCHA_IMAGE_PATH)}")
        print("***************** 验证码操作指南 *****************")
        print("1. 验证码图片已自动打开，请在图中点击正确的验证码（按顺序）。")
        print("2. 在下方终端中，按提示输入点击的坐标。")
        print("3. 坐标格式为 x1,y1,x2,y2,...，用英文逗号隔开。")
        print("   (例如: 45,51,105,120)")
        print("4. 如果图片未自动打开，请手动打开上述路径的图片。")
        print("**************************************************")

        # 获取用户输入
        captcha_input = input("请输入验证码坐标: ")
        return captcha_input.strip()

    except Exception as e:
        print(f"❌ 处理验证码时出错: {e}")
        return ""
    finally:
        # 清理临时文件
        if os.path.exists(CAPTCHA_IMAGE_PATH):
            try:
                os.remove(CAPTCHA_IMAGE_PATH)
            except OSError as e:
                print(f"❌ 无法删除临时验证码文件 {CAPTCHA_IMAGE_PATH}: {e}") 