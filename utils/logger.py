# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/7/22 15:11
@Desc     : 日志工具
"""

# 日志配置import logging
import os
from datetime import datetime
import logging

# 日志目录
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# 日志文件名
log_file = os.path.join(LOG_DIR, f"{datetime.now().strftime('%Y-%m-%d')}.log")

# 日志格式
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"

# 日志配置
logging.basicConfig(
    level=logging.INFO,  # 默认级别（可改为 DEBUG）
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler()  # 控制台输出
    ]
)

# 创建一个通用 logger 实例
logger = logging.getLogger("12306Spider")


if __name__ == "__main__":
    logger.info("日志模块测试：这是一次 info 级别的日志。")
    logger.warning("日志模块测试：这是一次 warning 级别的日志。")
    logger.error("日志模块测试：这是一次 error 级别的日志。")