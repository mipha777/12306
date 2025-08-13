# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/7/22 15:09
@Desc     : 抢票逻辑（提交订单、选座等）
"""

import requests
from core.session_manager import SessionManager
from utils.headers_utils import build_dynamic_headers
import re
from collections import OrderedDict
import httpx
from utils.logger import logger

class TicketBuyer:
    def __init__(self, session_manager: SessionManager):
        self.sm = session_manager
        self.session = self.sm.get_session()
    # 先进行身份效验
    def ensure_user_login(self):
        CHECK_USER_URL = 'https://kyfw.12306.cn/otn/login/checkUser'
        headers = build_dynamic_headers({
            "Referer": "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc",
            "Origin": "https://kyfw.12306.cn"
        })
        data = '_json_att='
        try:
            resp = self.session.post(CHECK_USER_URL, headers=headers, data=data, timeout=10)
            resp.raise_for_status()
            result = resp.json()
            if result.get("status"):
                logger.info("身份验证成功！")
                return True
            else:
                logger.error(f"身份验证失败: {result.get('messages')}")
                return False
        except Exception as e:
            logger.warn(f"身份验证请求异常: {e}")
            return False

    def submit_order_request(self, secret_str, train_date, back_train_date, from_station, to_station,bed_level_info, cookies,purpose_codes="ADULT"):
        """
        提交订单请求（第一步）
        :param secret_str: 查票接口返回的加密字符串
        :param train_date: 出发日期，格式 YYYY-MM-DD
        :param back_train_date: 返程日期，格式 YYYY-MM-DD（通常与出发日期相同）
        :param from_station: 出发站代码
        :param to_station: 到达站代码
        :param purpose_codes: 乘客类型，默认 ADULT
        :return: True/False
        """

        url = "https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest"
        data = {
          "secretStr": secret_str,
          "train_date": train_date,
          "back_train_date": back_train_date,
          "tour_flag": "dc",
          "purpose_codes": purpose_codes,
          "query_from_station_name": from_station,
          "query_to_station_name": to_station,
          "bed_level_info": bed_level_info,
          "seat_discount_info": "",
          "undefined": ""
        }

        headers = OrderedDict([
            ("Host", "kyfw.12306.cn"),
            ("Connection", "keep-alive"),
            ("sec-ch-ua-platform", "\"Windows\""),
            ("X-Requested-With", "XMLHttpRequest"),
            ("User-Agent",
             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"),
            ("Accept", "*/*"),
            ("sec-ch-ua", "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\""),
            ("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8"),
            ("sec-ch-ua-mobile", "?0"),
            ("Origin", "https://kyfw.12306.cn"),
            ("Sec-Fetch-Site", "same-origin"),
            ("Sec-Fetch-Mode", "cors"),
            ("Sec-Fetch-Dest", "empty"),
            ("Referer","https://kyfw.12306.cn/otn/leftTicket/init"),
            ("Accept-Encoding", "gzip, deflate, br, zstd"),
            ("Accept-Language", "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"),
            ("Cookie",cookies)
        ])
        try:
            with httpx.Client(http1=True) as client:  # http1=True 必须 防止乱序
                resp = client.post(url, headers=headers, data=data)
                resp.raise_for_status()
                result = resp.json()
                if result.get("status"):
                    print("提交购票请求成功！")
                    return True
                else:
                    print(f"提交购票请求失败: {result.get('messages')}")
                    return '203'
        except Exception as e:
            print(f"提交购票请求异常: {e}")
            if '302' in str(e):
                return '302'
            else:
                return False

    def init_dc(self,cookies):
        """
        初始化订单确认页面（第二步）
        需要在提交订单后调用。
        :return: dict，包含页面初始化返回的所有参数（如REPEAT_SUBMIT_TOKEN等）
        """
        url = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"
        headers = OrderedDict([
            ("Host", "kyfw.12306.cn"),
            ("Connection", "keep-alive"),
            ("Content-Length", "10"),
            ("Cache-Control", "max-age=0"),
            ("sec-ch-ua", "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\""),
            ("sec-ch-ua-mobile", "?0"),
            ("sec-ch-ua-platform", "\"Windows\""),
            ("Origin", "https://kyfw.12306.cn"),
            ("Content-Type", "application/x-www-form-urlencoded"),
            ("Upgrade-Insecure-Requests", "1"),
            ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"),
            ("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"),
            ("Sec-Fetch-Site", "same-origin"),
            ("Sec-Fetch-Mode", "navigate"),
            ("Sec-Fetch-User", "?1"),
            ("Sec-Fetch-Dest", "document"),
            ("Referer",
             "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E9%83%91%E5%B7%9E%E4%B8%9C,ZAF&ts=%E8%A5%BF%E5%AE%89,XAY&date=2025-08-01&flag=N,N,Y"),
            ("Accept-Encoding", "gzip, deflate, br, zstd"),
            ("Accept-Language", "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"),
            ("Cookie", cookies)
        ])
        data = {"_json_att": ""}
        try:
            with httpx.Client(http1=True) as client:  # http1=True 必须 防止乱序
                resp = client.post(url, headers=headers, data=data)
                resp.raise_for_status()
                content_type = resp.headers.get("content-type", "")
                if "text/html" in content_type:  # HTML 页面
                    print("订单确认页面初始化成功")
                    return resp.text
                elif "application/json" in content_type:
                    result = resp.json()
                    if result.get("status"):
                        print("订单确认页面初始化成功！")
                        return result
                    else:
                        print(f"订单确认页面初始化失败: {result.get('messages')}")
                        return None
                else:
                    print(f"订单确认页面返回未知格式：{content_type}")
                    return resp.text
        except Exception as e:
            if '302' in str(e):
                print(f"重新登录")
            return False
        
    def get_passenger_dtos(self, repeat_submit_token,cookies):
        """
        获取乘客信息（第三步）
        :param repeat_submit_token: 上一步提取的 token
        :return: 乘客信息列表
        """
        url = "https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs"
        headers = OrderedDict([
            ("Host", "kyfw.12306.cn"),
            ("Connection", "keep-alive"),
            ("sec-ch-ua-platform", "\"Windows\""),
            ("X-Requested-With", "XMLHttpRequest"),
            ("User-Agent",
             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"),
            ("Accept", "*/*"),
            ("sec-ch-ua", "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\""),
            ("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8"),
            ("sec-ch-ua-mobile", "?0"),
            ("Origin", "https://kyfw.12306.cn"),
            ("Sec-Fetch-Site", "same-origin"),
            ("Sec-Fetch-Mode", "cors"),
            ("Sec-Fetch-Dest", "empty"),
            ("Referer", "https://kyfw.12306.cn/otn/confirmPassenger/initDc"),
            ("Accept-Encoding", "gzip, deflate, br, zstd"),
            ("Accept-Language", "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"),
            ("Cookie", cookies)
        ])
        data = {"_json_att": "", "REPEAT_SUBMIT_TOKEN": repeat_submit_token}
        try:
            with httpx.Client(http1=True) as client:  # http1=True 必须 防止乱序
                resp = client.post(url, headers=headers, data=data)
                resp.raise_for_status()
                result = resp.json()
                if result.get("status"):
                    print("获取乘客信息成功")
                    return result
                else:
                    print(f"获取乘客信息失败: {result.get('messages')}")
                    return False
        except Exception as e:
            print(f"获取乘客信息请求异常: {e}")
            return False

    def check_order_info(self, passenger_ticket_str, old_passenger_str, repeat_submit_token, cookies):
        """
        检查订单信息（第四步）
        :param passenger_ticket_str: 乘客票信息字符串
        :param old_passenger_str: 旧乘客信息字符串
        :param repeat_submit_token: token
        :return: True/False

        """
        url = "https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo"
        headers = OrderedDict([
            ("Host", "kyfw.12306.cn"),
            ("Connection", "keep-alive"),
            ("sec-ch-ua-platform", "\"Windows\""),
            ("X-Requested-With", "XMLHttpRequest"),
            ("User-Agent",
             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"),
            ("Accept", "application/json, text/javascript, */*; q=0.01"),
            ("sec-ch-ua", "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\""),
            ("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8"),
            ("sec-ch-ua-mobile", "?0"),
            ("Origin", "https://kyfw.12306.cn"),
            ("Sec-Fetch-Site", "same-origin"),
            ("Sec-Fetch-Mode", "cors"),
            ("Sec-Fetch-Dest", "empty"),
            ("Referer", "https://kyfw.12306.cn/otn/confirmPassenger/initDc"),
            ("Accept-Encoding", "gzip, deflate, br, zstd"),
            ("Accept-Language", "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"),
            ("Cookie",cookies)
             ])

        data = {
            "cancel_flag": "2",
            "bed_level_order_num": "000000000000000000000000000000",
            "passengerTicketStr": passenger_ticket_str,
            "oldPassengerStr": old_passenger_str,
            "tour_flag": "dc",
            "whatsSelect": "1",
            "sessionId": "",
            "sig": "",
            "scene": "nc_login",
            "_json_att": "",
            "REPEAT_SUBMIT_TOKEN": repeat_submit_token
        }
        try:
            resp = self.session.post(url, data=data, headers=headers, timeout=10)
            resp.raise_for_status()
            result = resp.json()
            if result.get("status"):
                print("订单信息检查通过！")
                return True
            else:
                print(f"订单信息检查失败: {result.get('messages')}")
                return False
        except Exception as e:
            print(f"订单信息检查异常: {e}")
            return False

    def confirm_single_for_queue(self,cookies, passengerTicketStr, oldPassengerStr, key_check_isChange, leftTicketStr,train_location,REPEAT_SUBMIT_TOKEN, choose_seats='', seatDetailType='000', is_jy='N', is_cj='Y',encryptedData='',whatsSelect='1',roomType='00',dwAll='N',_json_att='', purpose_codes='00'):
        """
        确认排队 第五步
        :param train_date: 时间
        :param train_no: 车辆内部编号
        :param stationTrainCode: 车次
        :param seatType: 座位类型  1：硬座 2：硬卧 3：软卧 4：硬卧+软卧
        :param fromStationTelecode: 出发站
        :param toStationTelecode: 到达站
        :param leftTicket: 查票接口返回的 leftTicketStr，需双重 urlencode
        :param purpose_codes: 00：成人 01：儿童 02：学生 03：军人
        :param train_location: 查票接口返回的 train_location
        :param repeat_submit_token: token
        :param encrypted_data: 默认空
        :param is_jy: 是否军人（默认N）
        :param is_cj: 是否残疾（默认Y）
        :return: True/False

        """
        import urllib.parse
        url = "https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue"
        headers = OrderedDict([
            ("Host", "kyfw.12306.cn"),
            ("Connection", "keep-alive"),
            ("sec-ch-ua-platform", "\"Windows\""),
            ("X-Requested-With", "XMLHttpRequest"),
            ("User-Agent",
             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"),
            ("Accept", "application/json, text/javascript, */*; q=0.01"),
            ("sec-ch-ua", "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\""),
            ("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8"),
            ("sec-ch-ua-mobile", "?0"),
            ("Origin", "https://kyfw.12306.cn"),
            ("Sec-Fetch-Site", "same-origin"),
            ("Sec-Fetch-Mode", "cors"),
            ("Sec-Fetch-Dest", "empty"),
            ("Referer", "https://kyfw.12306.cn/otn/confirmPassenger/initDc"),
            ("Accept-Encoding", "gzip, deflate, br, zstd"),
            ("Accept-Language", "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"),
            ("Cookie", cookies)
        ])
        
        data = {
            "passengerTicketStr": passengerTicketStr,
            "oldPassengerStr": oldPassengerStr,
            "purpose_codes": "00",
            "key_check_isChange": key_check_isChange,
            "leftTicketStr": leftTicketStr,
            "train_location": train_location,
            "choose_seats": "",
            "seatDetailType": "000",
            "is_jy": "N",
            "is_cj": "Y",
            "encryptedData": "",
            "whatsSelect": "1",
            "roomType": "00",
            "dwAll": "N",
            "_json_att": "",
            "REPEAT_SUBMIT_TOKEN": REPEAT_SUBMIT_TOKEN
        }
        try:
            resp = self.session.post(url, data=data, headers=headers, timeout=10)
            # status_code = resp.status_code  # 获取状态码
            resp_data = resp.json().get("data", {})  # 解析返回 JSON
            submit_status = resp_data.get("submitStatus", None)
            if submit_status:
                logger.info("排队确认成功！")
                return True
            else:
                logger.error(f"排队确认失败: {resp_data.get("errMsg", None)}")
                return False
        except Exception as e:
            logger.error(f"排队确认异常: {e}")
            return False

    def query_order_wait_time(self, repeat_submit_token):
        """
        查询排队/订单等待时间（第六步）
        :param repeat_submit_token: token
        :param order_sequence_no: 订单号
        :return: 剩余等待时间/订单状态
        """
        url = "https://kyfw.12306.cn/otn/confirmPassenger/queryOrderWaitTime"
        headers = build_dynamic_headers({
            "Referer": "https://kyfw.12306.cn/otn/confirmPassenger/initDc"
        })
        params = {
            "random": requests.utils.default_headers()['User-Agent'],
            "tourFlag": "dc",
            "_json_att": "",
            "REPEAT_SUBMIT_TOKEN": repeat_submit_token,
        }
        print()
        try:
            resp = self.session.get(url, params=params, headers=headers, timeout=10)
            resp.raise_for_status()
            result = resp.json()
            print("查询排队/订单等待时间成功！")
            return result.get("data", {}).get("orderId")
        except Exception as e:
            print(f"查询排队/订单等待时间异常: {e}")
            return None

    def result_order_for_dc_queue(self, repeat_submit_token, order_sequence_no):
        """
        查询订单结果（第七步）
        :param repeat_submit_token: token
        :param order_sequence_no: 订单号
        :return: 订单结果
        """
        url = "https://kyfw.12306.cn/otn/confirmPassenger/resultOrderForDcQueue"
        headers = build_dynamic_headers({
            "Referer": "https://kyfw.12306.cn/otn/confirmPassenger/initDc"
        })
        data = {
            "orderSequence_no": order_sequence_no,
            "_json_att": "",
            "REPEAT_SUBMIT_TOKEN": repeat_submit_token
        }
        try:
            resp = self.session.post(url, data=data, headers=headers, timeout=10)
            resp.raise_for_status()
            result = resp.json()
            print("查询订单结果成功！")
            return result.get("data", {})
        except Exception as e:
            print(f"查询订单结果异常: {e}")
            return None

