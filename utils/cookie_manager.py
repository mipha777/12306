# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/7/24 15:50
@Desc     : 
"""
import os
from core.session_manager import SessionManager
from utils.get_nested_value import get_nested_value_fun
from utils.logger import logger
from datetime import date
# from core.login_handler import LoginHandler
def cookie_manager(config):
    # 第一步 配置验证
    required_keys = ['ticket_info.from_station', 'ticket_info.to_station',
                     'ticket_info.train_date','ticket_info.train_date_true','ticket_info.train_time_true']
    for key in required_keys:
        if not get_nested_value_fun(config, key):
            logger.error(f"配置错误: 缺少必要参数 {key} 程序自动退出")
            exit()
    ticket_config = config.get("ticket_info", {})  # 获取车票配置
    from_station = ticket_config.get("from_station")  # 起始站 中文
    to_station = ticket_config.get("to_station")  # 终点站 中文
    train_date = ticket_config.get("train_date")  # 有票的日期
    train_date_true = ticket_config.get("train_date_true")  # 票的日期
    back_train_date = date.today().strftime("%Y-%m-%d")  # 转为字符串
    passengers = config.get('passengers', {})['name'] # 乘车人名字
    # 第二步：登录或加载 session
    session_manager = SessionManager(passengers)
    if session_manager.load_cookies():
        logger.info("成功加载 cookie，使用已有登录信息。")
    else:
        logger.info("无可用 cookie，正在打开浏览器进行登录...")
        cookies = session_manager.load_cookies()

        try:
            if cookies:
                logger.info("登录成功，cookie 已保存。")
                session_manager.save_cookies()
            else:
                logger.error("登录失败，你没登录完成为啥要关浏览器？")
                logger.info("程序退出")
        except Exception as e:
            logger.error(f"登录过程发生异常：{str(e)}")
    return session_manager, train_date, back_train_date, from_station, to_station,train_date_true,passengers

