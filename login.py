# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/7/22 14:18
@Desc     : 使用Playwright登录 获取cookie
"""

import yaml
import asyncio
import os
from utils.logger import logger
from playwright.async_api import async_playwright
from playwright_stealth import Stealth
from core.session_manager import SessionManager, ua

CONFIG_FILE = "config.yaml"
LOGIN_URL = "https://kyfw.12306.cn/otn/resources/login.html"
USER_CENTER_URL = "https://kyfw.12306.cn/otn/view/index.html"
BROWSER_DATA_DIR = "browser_data"


async def main():
    """
    1. 尝试直接访问用户中心，如果已登录，则刷新cookie并退出。
    2. 如果未登录，则等待用户手动登录，然后保存cookie。
    """
    # 1. 加载配置获取用户名
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        username = config.get('passengers', {})['name']
        if not username or username == "your_username":
            logger.error("请先在config.yaml文件中配置您的12306用户名。")
            return
    except FileNotFoundError:
        logger.error(f"配置文件{CONFIG_FILE}不存在。")
        return
    except Exception as e:
        logger.error(f"加载配置文件时出错:{e}")
        return

    # 确保浏览器数据目录存在
    os.makedirs(BROWSER_DATA_DIR, exist_ok=True)
    session_manager = SessionManager(username)

    # 2. 启动带持久化上下文的浏览器
    async with async_playwright() as p:
        # 创建Stealth实例
        stealth = Stealth()

        context = await p.chromium.launch_persistent_context(
            BROWSER_DATA_DIR,
            headless=False,
            slow_mo=100,
            user_agent=ua.random,
            # 伪装参数
            viewport={'width': 1920, 'height': 1080}, # 设置标准分辨率
            locale='zh-CN',                          # 设置为中文
            timezone_id='Asia/Shanghai',             # 设置为东八区时区
            args=['--disable-blink-features=AutomationControlled'] # 禁用自动化标志
        )
        
        # 将 stealth 应用到上下文中
        await stealth.apply_stealth_async(context)
        page = await context.new_page()

        try:
            logger.info("正在检查登录状态...")
            await page.goto(USER_CENTER_URL, timeout=15000)
            # 等待片刻，让页面加载
            await page.wait_for_timeout(2000)

            # 检查当前 URL 判断是否已登录
            if LOGIN_URL in page.url:
                logger.info("登录已失效，请在浏览器中手动完成登录操作。")
                # 等待用户登录成功后跳转到用户中心
                await page.wait_for_url(f"{USER_CENTER_URL}*", timeout=300 * 1000)
                logger.info("登录成功！")
            else:
                logger.info("检测到您已登录。")

            # 无论之前是否登录，都刷新一下cookie
            logger.info("正在刷新并保存cookie...")
            cookies = await context.cookies()
            cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies}
            session_manager.save_cookies(cookies_dict)
            logger.info("Cookie已更新！现在可用于抢票。")

        except Exception as e:
            logger.error(f"操作过程中出现错误: {e}")
        finally:
            # 自动关闭
            logger.info("登录流程完成，自动关闭浏览器...")
            await context.close()
            return True, cookies_dict  # 表示登录成功，返回 cookie 字典

def login_handler():
    # 使用异步的事件循环管理
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    login_success, browser_cookies = loop.run_until_complete(main())
    if login_success:
        return browser_cookies
    return None

