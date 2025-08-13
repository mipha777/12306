# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/7/22 15:08
@Desc     : 核心查票逻辑
"""

import json
import urllib.parse
from core.session_manager import SessionManager
from utils.headers_utils import build_dynamic_headers




class TicketQuerier:
    def __init__(self, session_manager: SessionManager, station_map_path="data/station_name_map.json"):
        self.sm = session_manager
        self.session = self.sm.get_session()
        self._load_station_map(station_map_path)


    def _load_station_map(self, station_map_path: str):
        """加载车站名到代码的映射"""
        try:
            with open(station_map_path, 'r', encoding='utf-8') as f:
                self.station_map = json.load(f)
        except Exception as e:
            print(f"加载车站映射文件失败: {e}")
            self.station_map = {}

    def _get_station_code(self, station_name: str) -> str:
        """根据中文名获取车站代码"""
        return self.station_map.get(station_name, "")

    def _get_cookie_station_val(self, station_name: str, station_code: str) -> str:
        """
        生成 cookie 中需要的车站值，格式为 "URL编码的中文名,车站代码"
        例如: 广州,GZQ -> %E5%B9%BF%E5%B7%9E,GZQ
        """
        # 从您的日志分析，cookie 中保存的站名部分是 URL 编码
        encoded_name = urllib.parse.quote(station_name)
        return f"{encoded_name},{station_code}"

    def parse_ticket_data(self, raw_data):
        print("查询结果分析：")
        # print(raw_data)
        result_list = raw_data.get('result', [])
        if not result_list:
            print(" -----> 未查询到符合条件的车次。")
            return
        print(f"当天共查询到 {len(result_list)} 趟列车。")
        # 这里返回所有的查询到的车辆的信息列表
        return result_list # list
        



    def lookfor(self, from_station_name: str, to_station_name: str, train_date: str,back_train_date:str):
        """
        执行一次查票请求

        :param from_station_name: 出发站中文名
        :param to_station_name: 到达站中文名
        :param train_date: 出发日期，格式 "YYYY-MM-DD"
        :return: 接口返回的原始 JSON 数据，或在失败时返回 None
        """
        # 查票接口 URL
        QUERY_URL = "https://kyfw.12306.cn/otn/leftTicket/queryU"
        # 1. 获取车站代码
        from_station_code = self._get_station_code(from_station_name)
        to_station_code = self._get_station_code(to_station_name)
        if not all([from_station_code, to_station_code]):
            print("出发站或到达站不存在于映射文件中。")
            return None

        # 2. 更新查询 Cookie
        # 根据您的日志，cookie值是 url编码后的中文,车站代码
        from_cookie_val = f"{urllib.parse.quote(from_station_name)},{from_station_code}"
        to_cookie_val = f"{urllib.parse.quote(to_station_name)},{to_station_code}"
        self.sm.update_query_cookies(from_cookie_val, to_cookie_val, train_date,back_train_date)

        # 3. 构建请求参数和请求头
        params = {
            "leftTicketDTO.train_date": train_date,
            "leftTicketDTO.from_station": from_station_code,
            "leftTicketDTO.to_station": to_station_code,
            "purpose_codes": "ADULT"
        }
        # 参照您抓包的日志，构建高仿真请求头
        referer_url = (f"https://kyfw.12306.cn/otn/leftTicket/init?"
                       f"linktypeid=dc&fs={from_cookie_val}&ts={to_cookie_val}&date={train_date}&flag=N,N,Y")
        # 动态生成 sec-ch-ua
        ua_parts = self.session.headers['User-Agent'].split(' ')
        brand_parts = [part for part in ua_parts if
                       '/' in part and 'like' not in part and 'Gecko' not in part and 'AppleWebKit' not in part and 'Mozilla' not in part]
        sec_ch_ua = ", ".join([f'"{p.split("/")[0]}";v="{p.split("/")[1].split(".")[0]}"' for p in brand_parts])
        sec_ch_ua = sec_ch_ua.replace('Edg', '"Microsoft Edge"')  # 特殊处理 Edge

        headers = {
            "Host": "kyfw.12306.cn",
            "Connection": "keep-alive",
            "Cache-Control": "no-cache",
            "sec-ch-ua-platform": '"Windows"',
            "sec-ch-ua": sec_ch_ua,
            "sec-ch-ua-mobile": "?0",
            "X-Requested-With": "XMLHttpRequest",
            "Accept": "*/*",
            "If-Modified-Since": "0",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": referer_url,
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
        }
        # 4. 发起请求
        try:
            print(f"正在查询 {train_date} 从 {from_station_name} 到 {to_station_name} 的车票...")
            resp = self.session.get(QUERY_URL, params=params, headers=headers, timeout=10)
            print(f"查票接口响应状态: {resp.status_code}")
            # 增强错误类型判断
            if 'html' in resp.headers.get('Content-Type', '') or resp.text.startswith('<!DOCTYPE html'):
                print("检测到登录失效，需要重新登录")
                return None
            elif resp.status_code == 403:
                print("服务器拒绝访问，可能是IP被限制")
                return None
            elif resp.status_code == 503:
                print("服务器暂时不可用，可能是访问过于频繁")
                return None
            resp.raise_for_status()
            # 修复：保存完整的Session Cookie而非仅查询Cookie
            self.sm.save_cookies()
            # 5. 解析结果
            result = resp.json()
            if result.get("status"):
                print("查询成功！")
                return self.parse_ticket_data(result.get("data", {})),from_station_code
            else:
                print(f"查询失败: {result.get('messages')}")
                return None
        except Exception as e:
            print(f"请求查票接口时发生错误: {e}")
            return None
