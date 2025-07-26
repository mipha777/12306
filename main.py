# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/7/22 14:18
@Desc     :  主程序入口（自动加载 cookie，执行查票 + 抢票
"""
import json
import yaml
import time
from datetime import datetime, timedelta
from login import login_handler
from core.session_manager import SessionManager
from core.lookfor_ticket import TicketQuerier
from core.Check_ticket import TicketFilter
from core.buy_ticket import TicketBuyer
from utils.logger import logger
from utils.get_nested_value import get_nested_value_fun, get_station_codes
from utils.token_parser import  *
from core.user_info import build_passenger_strings
from utils.cookie_manager import cookie_manager
from utils.headers_utils import back_last_cookies,back_cookies
from utils.clean_cookies import cookies_clean
# 加载配置
def load_config(path='config.yaml'):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def main():
    logger.info("大帅比的程序开始运行!!!!!!!!!!!!!!!!!")
    logger.info("大帅比的程序开始运行!!!!!!!!!!!!!!!!!")
    try:
        # 第一步：读取配置文件
        config = load_config()
        train_time_true = config["ticket_info"]["train_time_true"]
        # 1. 转换为 datetime 对象（加上今天的日期）
        start_time = datetime.strptime(train_time_true, "%H:%M:%S")
        # 2. 减去 3 分钟
        start_time = start_time - timedelta(minutes=3)
        # 3. 获取前3分钟的时间（字符串格式）
        new_time_str = start_time.time()
        while True:
            now = datetime.now().time()
            if now >= new_time_str:
                print(f"------到达开售前三分钟，开始进行抢票前准备---------------")
                break
        time.sleep(1)
        print('准备 1')
        time.sleep(1)
        print('准备 2')
        time.sleep(1)
        print('准备 3')

        session_manager, train_date, back_train_date, from_station, to_station,train_date_true = cookie_manager(config)
        # 第三步：查询车票
        query = TicketQuerier(session_manager=session_manager)

        tickets,from_station_code = query.lookfor(
            from_station_name=from_station,
            to_station_name=to_station,
            train_date=train_date,
            back_train_date = back_train_date
        )# tickets 为 list
        print(len(tickets))

        # 车票筛选 筛选出符合条件的车票
        ticket_filter = TicketFilter(config_path='config.yaml')
        filtered_tickets = ticket_filter.filter_tickets(tickets,from_station_code)
        print(f'筛选完成 共有{len(filtered_tickets)}辆车次符合条件')
        # 对筛选后的车票进行购买

        ticket_buyer = TicketBuyer(session_manager)
        # 1.身份效验
        ticket_buyer.ensure_user_login()
        print('身份效验完成')
        # print(secret_str,train_date,back_train_date,from_station,to_station)
        # 2.提交订单请求
        cookies = back_cookies() # 获取最新的cookie
        Order_request = ticket_buyer.submit_order_request(
            secret_str=filtered_tickets[0]['secretStr'],
            train_date=train_date,
            back_train_date=back_train_date,
            from_station=from_station,
            to_station=to_station,
            bed_level_info=filtered_tickets[0]['bed_level_info'],
            cookies=cookies
        )
        if Order_request == '302':
            logger.error('订单请求提交第一步失败')
            print('登录身份信息过期 请重新登录')
            cookies_clean()
            exit() # 这里后期衔接重新登录函数
        elif Order_request == '203':
            logger.info('订单请求失败 需要重新发起订单请求')
            exit() # 这里后期重新发起请求 发起三次均失败 则会重新启动程序
        else:
            logger.info('订单初步请求成功')

        # 3. 初始化订单确认页面并提取 token
        dc_html_json = ticket_buyer.init_dc(cookies=cookies)
        dc_html = json.dumps(dc_html_json)
        RepeatSubmitToken,key_check_isChange,train_location,leftTicket,train_no = html_prase(dc_html)
        # 重要步骤# 重要步骤# 重要步骤# 重要步骤# 重要步骤# 重要步骤# 重要步骤# 重要步骤# 重要步骤# 重要步骤# 重要步骤# 重要步骤# 重要步骤# 重要步骤
        print(RepeatSubmitToken,key_check_isChange,train_location,leftTicket,train_no)
        # 4. 获取乘客信息
        response_json = ticket_buyer.get_passenger_dtos(RepeatSubmitToken,cookies=cookies)
        # 5. 构建乘客信息字符串（需从 user_info.py 导入 build_passenger_strings）
        p_str, op_str = build_passenger_strings(config, response_json)
        # # 6. 检查订单信息
        ticket_buyer.check_order_info(p_str, op_str, RepeatSubmitToken)


        # p_str = '3,0,1,李浩歌,1,4127***********634,188****2698,N,1be6b8b1e436f0de43998e478148524d20ac2bc947d2b58d3218a4b10eae8f4efc0cf22e751e14cedeb261b42fb95c637064a5591b72b58314cebc71cdf405e1dee4af3f0947645264e03dea190d5e32'
        # op_str = '李浩歌,1,4127***********634,1_'
        # === 等待到指定时间 ===

        target_time = datetime.strptime(train_time_true, "%H:%M:%S").time()
        print(f"等待时间点：{target_time_str}")

        while True:
            now = datetime.now().time()
            if now >= target_time:
                print(f"--------------到达指定时间：{now}，开始抢票------------")
                break
            time.sleep(1)

        cookies = back_last_cookies(train_date_true) # 改变cookies的日期
        dc_html_json = ticket_buyer.init_dc(cookies=cookies)
        dc_html = json.dumps(dc_html_json)
        # 提取相关参数
        RepeatSubmitToken, key_check_isChange, train_location, leftTicket, train_no = html_prase(dc_html)
        # 7. 确认排队（需从 ticket 提取相关参数）
        result = ticket_buyer.confirm_single_for_queue(
            passengerTicketStr=p_str,
            oldPassengerStr=op_str,
            key_check_isChange=key_check_isChange,
            leftTicketStr=leftTicket,
            train_location=train_location,
            REPEAT_SUBMIT_TOKEN=RepeatSubmitToken
        )
        print(result)
        if result:
            # 8. 查询订单结果（轮询）
            for _ in range(10):
                status = ticket_buyer.query_order_wait_time(RepeatSubmitToken)
                if status and status != 'null':
                    print("购票成功！")
                    break
                time.sleep(1)
    except Exception as e:
        print(f"程序执行出错: {str(e)}")
        # 记录详细错误日志
        logger.error(f"Main execution failed: {str(e)}", exc_info=True)
        return


if __name__ == "__main__":
    main()
