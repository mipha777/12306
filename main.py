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
from utils.get_nested_value import get_station_codes
from utils.token_parser import  *
from core.user_info import build_passenger_strings
from utils.cookie_manager import cookie_manager
from utils.headers_utils import back_chance_cookies,back_cookies,back_last_buy_cookie
from utils.clean_cookies import cookies_clean
# 加载配置
def load_config(path='config.yaml'):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def main():
    print("大帅比的程序开始运行!!!!!!!!!!!!!!!!!")
    logger.info("大帅比的程序开始运行!!!!!!!!!!!!!!!!!")
    try:
        # 第一步：读取配置文件
        config = load_config()
        train_time_true = config["ticket_info"]["train_time_true"]
        start_time = datetime.strptime(train_time_true, "%H:%M:%S")
        start_time = start_time - timedelta(minutes=3)
        new_time_str = start_time.time()
        while True:
            now = datetime.now().time()
            if now >= new_time_str:
                print(f"------到达开售前三分钟，开始进行抢票前准备工作---------------")
                logger.info(f"------到达开售前三分钟，开始进行抢票前准备工作---------------")
                break
        logger.info('正在进行浏览器初始化并检查配置')
        def Load_the_configuration(config):
            return cookie_manager(config)
        session_manager, train_date, back_train_date, from_station, to_station, train_date_true, passengers = Load_the_configuration(config)
        time.sleep(2.12)
        # 第二步：查询车票
        query = TicketQuerier(session_manager=session_manager)
        tickets,from_station_code = query.lookfor(
            from_station_name=from_station,
            to_station_name=to_station,
            train_date=train_date,
            back_train_date = back_train_date
        )# tickets 为 list
        logger.info(f'当天共查到{len(tickets)} 辆车')

        def Awesome_screening_mechanism():
            # 第三步 车票筛选 筛选出符合条件的车票
            ticket_filter = TicketFilter(config_path='config.yaml')
            return ticket_filter.filter_tickets(tickets,from_station_code)
        filtered_tickets = Awesome_screening_mechanism()
        # 第四步 对筛选后的车票进行购买前操作流程
        time.sleep(1.98)
        ticket_buyer = TicketBuyer(session_manager)
            # 4.1 身份效验
        Authentication_results = ticket_buyer.ensure_user_login()
        if Authentication_results:
            logger.info('身份效验完成，已进入购票流程')
            print('身份效验完成')
        else:
            cookies_clean()
            session_manager, train_date, back_train_date, from_station, to_station, train_date_true, passengers = Load_the_configuration(config)
        time.sleep(2.124)
            # 4.2 提交订单初步请求
        cookies = back_cookies()
        def Order_initialization(filtered_tickets,train_date_ture,back_train_date,from_station,to_station,cookies):
            Order_request = ticket_buyer.submit_order_request(secret_str=filtered_tickets[0]['secretStr'],train_date=train_date_ture,back_train_date=back_train_date,from_station=from_station,to_station=to_station,bed_level_info=filtered_tickets[0]['bed_level_info'],cookies=cookies)
             # Order_initialization(filtered_tickets,train_date,back_train_date,from_station,to_station)
            if Order_request == '302':
                logger.error('订单请求提交第一步失败 登录身份信息过期 请重新登录') # 身份效验过后 这里一搬不会出现问题 除非是请求太频繁
                print('登录身份信息过期 请重新登录')
                cookies_clean()
                Load_the_configuration(config)
                Order_initialization(filtered_tickets,train_date,back_train_date,from_station,to_station,cookies)
            elif Order_request == '203':
                logger.info('订单请求失败 需要重新发起订单请求')
                Order_initialization(filtered_tickets, train_date, back_train_date, from_station, to_station,cookies)
            else:
                logger.info('订单初步请求成功')
        Order_initialization(filtered_tickets,train_date,back_train_date,from_station,to_station,cookies)
            # 4.3 初始化订单确认页面并提取 token

        def Extract_parameters(cookies):
            dc_html_json = ticket_buyer.init_dc(cookies=cookies)
            dc_html = json.dumps(dc_html_json)
            return html_prase(dc_html)
        time.sleep(1.253)
        RepeatSubmitToken, key_check_isChange, train_location, leftTicket = Extract_parameters(cookies)
        def Passenger_parameter_acquisition(RepeatSubmitToken,cookies):
                # 4.4 获取乘客信息
            time.sleep(1.177)
            response_json = ticket_buyer.get_passenger_dtos(RepeatSubmitToken,cookies)
                # 4.5 构建乘客信息字符串（需从 user_info.py 导入 build_passenger_strings）
            p_str, op_str = build_passenger_strings(config,passengers, response_json)
                # 4.6 检查订单信息
            time.sleep(1.281)
            ticket_buyer.check_order_info(p_str, op_str, RepeatSubmitToken,cookies)
            return p_str, op_str
        p_str, op_str = Passenger_parameter_acquisition(RepeatSubmitToken,cookies)


        # 第五步 等待时间 进行抢票
        target_time = datetime.strptime(train_time_true, "%H:%M:%S").time()
        print(f"开售时间点:{target_time}.....正在等待中.....")
        logger.info(f'设定的时间点为{target_time}...等待开售...')
        back_last_buy_cookie()  # 去除cookie内多余的参数
        cookies = back_chance_cookies(train_date_true)  # 赋值真正的抢票时间
        input()
        while True:
            now = datetime.now().time()
            if now >= target_time:
                print(f"--------------到达指定时间：{now}，开始抢票---------------")
                break
        start_time = time.time()  # 记录开始时间
            # 5.1 重新设定日期参数 将目标日期参数放入其中
        Order_initialization(filtered_tickets, train_date_true, back_train_date, from_station, to_station,cookies)
        RepeatSubmitToken, key_check_isChange, train_location, leftTicket = Extract_parameters(cookies)
            # 5.3 确认排队（需从 ticket 提取相关参数）
        def Grab_it(cookies,p_str,op_str,key_check_isChange,leftTicket,train_location,RepeatSubmitToken):
            result = ticket_buyer.confirm_single_for_queue(cookies=cookies , passengerTicketStr=p_str,oldPassengerStr=op_str,key_check_isChange=key_check_isChange,leftTicketStr=leftTicket,train_location=train_location,REPEAT_SUBMIT_TOKEN=RepeatSubmitToken)
            if result:
                return True
            return False

        it = 1
        while it <= 3 :
            result = Grab_it(cookies,p_str,op_str,key_check_isChange,leftTicket,train_location,RepeatSubmitToken)
            logger.info(f"正在进行第{it}次购买")
            if result:
                logger.info("购买成功，请尽快在手机上检查订单并支付")
                break
            logger.error(f"第{it}次购买失败")
            it += 1
        if it > 3:
            logger.error("三次购买尝试失败 他们太快啦！！")

        end_time = time.time()  # 记录结束时间
        logger.info(f'购票流程用时:{end_time - start_time:.4f} 秒')
        logger.info(f'购票流程结束:准备清除用户信息')
        time.sleep(10)
        cookies_clean()
        logger.info(f'程序结束:已清除用户信息')

    except Exception as e:
        print(f"程序执行出错: {str(e)}")
        cookies_clean()
        # 记录详细错误日志
        logger.error(f"Main execution failed: {str(e)}", exc_info=True)


if __name__ == "__main__":
    main()
