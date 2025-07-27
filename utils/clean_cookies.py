# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/7/25 22:51
@Desc     : 
"""
import os
import shutil
from utils.logger import logger

current_path = os.path.abspath(__file__)
# 获取 utils 目录路径
utils_dir = os.path.dirname(current_path)
# 获取上一级目录（即 12306 目录）
project_root = os.path.dirname(utils_dir)
# 拼出 cookies 目录路径
cookies_dir = os.path.join(project_root, "cookies")
# 临时浏览器的路径
browser_path = os.path.join(project_root, "browser_data")
def cookies_clean():
    for filename in os.listdir(cookies_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(cookies_dir, filename)
            try:
                os.remove(file_path)
                print(f"已删除：{file_path}")
            except Exception as e:
                print(f"删除失败：{file_path}，错误：{e}")

    if os.path.exists(browser_path) and os.path.isdir(browser_path):
        try:
            shutil.rmtree(browser_path)
            logger.info(f"文件夹 {browser_path} 删除成功！")
        except PermissionError:
            logger.error(f"权限不足，无法删除 {browser_path}，请关闭占用程序或以管理员身份运行。")
    else:
        logger.error(f"{browser_path} 不存在或已删除")

if __name__ == '__main__': # 测试入口
    cookies_clean()