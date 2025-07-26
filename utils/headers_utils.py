from fake_useragent import UserAgent
import random
import os
import json
# 获取当前文件所在目录（即 utils/）
cur_dir = os.path.dirname(__file__)

# 拼出目标 JSON 文件路径：跳出一层到项目根，再进 data 文件夹
json_path = os.path.join(cur_dir, '..', 'cookies', 'woshidashuaibi.json')
json_path = os.path.abspath(json_path)
def build_dynamic_headers(base_headers=None):
    ua = UserAgent()
    user_agent = ua.random
    # 动态生成 sec-ch-ua
    # 简单仿真，实际可根据 user_agent 进一步细化
    sec_ch_ua = '\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"'
    sec_ch_ua_platform = '"Windows"'
    sec_ch_ua_mobile = '?0'
    # 读取最新的cookies
    with open(json_path, 'r', encoding='utf-8') as f:
        cookies = json.load(f)
    # 拼接成合法的 Cookie 字符串
    cookie_str = '; '.join([f'{k}={v}' for k, v in cookies.items()])

    headers = {
        "Host": "kyfw.12306.cn",
        "Connection": "keep-alive",
        "Content-Length": "no-cache",
        "sec-ch-ua-platform": sec_ch_ua_platform,
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": user_agent,
        "Accept": "*/*",
        "sec-ch-ua": sec_ch_ua,
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "sec-ch-ua-mobile": sec_ch_ua_mobile,
        "Origin": "https://kyfw.12306.cn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Accept-Encoding":  "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        'Cookie':cookie_str
        # Referer、Origin 等建议由 base_headers 传入
    }


    if base_headers:
        headers.update(base_headers)
    return headers

def back_last_cookies(from_station):
    # 读取最新的cookies
    with open(json_path, 'r', encoding='utf-8') as f:
        cookies = json.load(f)
    # 拼接成合法的 Cookie 字符串
    cookies['_jc_save_fromDate'] = from_station
    cookie_str = '; '.join([f'{k}={v}' for k, v in cookies.items()])
    return cookie_str

def back_last_buy_cookie():
    # 1. 读取 JSON 文件内容为字典
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # 2. 删除指定的键（如果存在）
    data.pop("_passport_session", None)
    data.pop("uamtk", None )
    # 3. 写回文件
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def back_cookies():
    # 读取最新的cookies
    with open(json_path, 'r', encoding='utf-8') as f:
        cookies = json.load(f)
    # 拼接成合法的 Cookie 字符串
    cookie_str = '; '.join([f'{k}={v}' for k, v in cookies.items()])
    return cookie_str