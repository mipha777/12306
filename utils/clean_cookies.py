# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/7/25 22:51
@Desc     : 
"""
import os
import shutil


def cookies_clean():
    log_path = os.path.join('..', 'cookies', 'woshidashuaibi.json')
    browser_path = os.path.join('..', 'browser_data')
    if os.path.exists(log_path):
        os.remove(log_path)
        print(f"已删除: {log_path}")
    else:
        print(f"未找到: {log_path}")
    if os.path.exists(browser_path) and os.path.isdir(browser_path):
        try:
            shutil.rmtree(browser_path)
            print(f"文件夹 {browser_path} 删除成功！")
        except PermissionError:
            print(f"权限不足，无法删除 {browser_path}，请关闭占用程序或以管理员身份运行。")
    else:
        print(f"{browser_path} 不存在或不是文件夹。")

if __name__ == '__main__':
    cookies_clean()