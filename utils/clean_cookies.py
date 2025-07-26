# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/7/25 22:51
@Desc     : 
"""
import os

def cookies_clean():
    files_to_delete = [
        "woshidashuaibi.json",
        "123456.json",
    ]
    for file in files_to_delete:
        if os.path.exists(file):
            os.remove(file)
            print(f"已删除: {file}")
        else:
            print(f"未找到: {file}")