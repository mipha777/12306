# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/7/22 15:07
@Desc     : requests.Session 封装，cookie 加载/保存
"""

import urllib.parse
import requests
import json
import os
import login
from fake_useragent import UserAgent
from utils.logger import logger
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


COOKIES_DIR = "cookies"
# 创建一个全局的 UserAgent 实例，以便在多个模块间共享
ua = UserAgent()


class SessionManager:
    """
    管理 requests.Session 对象，负责 Cookie 的加载与保存。
    """

    def __init__(self, username: str):
        logger.info(f"SessionManager 初始化，收到乘车用户名: {username!r}")
        assert username, "初始化 SessionManager 时，username 不能为空！"
        self.username = username
        self.session = requests.Session()
        # 使用动态生成的 User-Agent
        self.session.headers.update({
            "User-Agent": ua.random,
        })
        # 确保 cookies 目录存在
        os.makedirs(COOKIES_DIR, exist_ok=True)



    @property
    def _cookie_path(self) -> str:
        """获取当前用户 cookie 文件的路径"""
        logger.info(f"生成用户{self.username}的cookie文件")
        return os.path.join(COOKIES_DIR, f"{self.username}.json")

    def load_cookies(self) -> bool:
        """从本地文件加载 cookie 到 session"""
        cookie_path = self._cookie_path
        if os.path.exists(cookie_path):
            logger.info(f"正在从 {cookie_path} 加载 cookie...")
            try:
                with open(cookie_path, 'r') as f:
                    cookies = json.load(f)
                    self.session.cookies.update(cookies)
                logger.info("Cookie 加载成功")
                return True
            except json.JSONDecodeError:
                logger.error(f"Cookie 文件 {cookie_path} 格式错误，加载失败。")
                return False

        else:
            logger.info('未找到用户cookie信息')
            login.login_handler()
        return False

    def save_cookies(self, cookies_dict: dict = None):
        """
        保存 cookie 到本地文件。
        如果提供了 cookies_dict, 则保存它，否则保存 session 中的 cookie。
        """
        cookie_path = self._cookie_path
        logger.info(f"正在保存 cookie 到 {cookie_path}...")

        # 确定要保存的 cookie
        data_to_save = cookies_dict
        if data_to_save is None:
            data_to_save = self.session.cookies.get_dict()

        with open(cookie_path, 'w') as f:
            json.dump(data_to_save, f, indent=4)
        logger.info(f"Cookie 已成功保存。")

    def get_session(self) -> requests.Session:
        """获取当前的 session 实例"""
        return self.session
    
    def update_query_cookies(self, from_station: str, to_station: str, train_date: str,back_train_date:str):
        """
        根据查询信息，更新 session 中的 cookie。
        这对于模拟查询操作至关重要。

        :param from_station: 格式化后的出发站 cookie 值
        :param to_station: 格式化后的到达站 cookie 值
        :param train_date: 出发日期，格式 "YYYY-MM-DD"
        """

        self.session.cookies.set("_jc_save_wfdc_flag", "dc", domain="kyfw.12306.cn", path="/") # 单程票
        self.session.cookies.set("_jc_save_toStation", to_station, domain="kyfw.12306.cn", path="/") # 目标车站
        self.session.cookies.set("_jc_save_toDate", back_train_date, domain="kyfw.12306.cn", path="/") # 运行日趋
        self.session.cookies.set("_jc_save_showIns", "true", domain="kyfw.12306.cn", path="/")
        self.session.cookies.set("_jc_save_fromDate", train_date, domain="kyfw.12306.cn", path="/") #车辆日期
        self.session.cookies.set("_jc_save_fromStation", from_station, domain="kyfw.12306.cn", path="/") # 开始车站




        # 打印时解码，方便查看
        from_station_decoded = urllib.parse.unquote(from_station.split(',')[0])
        to_station_decoded = urllib.parse.unquote(to_station.split(',')[0])
        logger.info(f"已更新查询 Cookie：从 {from_station_decoded} 到 {to_station_decoded}，日期 {train_date}")



