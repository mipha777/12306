# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/7/22 15:10
@Desc     : 筛选符合要求的车次
"""

import yaml
from pathlib import Path
import urllib.parse

class TicketFilter:
    def __init__(self, config_path="config.yaml"):
        self.config = self.load_config(config_path)
        self.ticket_info = self.config.get("ticket_info", {})
        self.travel_cfg = self.config.get("travel", {})

    def load_config(self, path: str) -> dict:
        """加载配置文件"""
        with open(Path(path), "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def filter_tickets(self, tickets: list[dict],from_station_code) -> list[dict]:
        """根据配置筛选车票"""
        preferred_trains = self.ticket_info.get("preferred_trains", [])
        seat_priority = self.ticket_info.get("seat_priority", [])
        # sleeper_preference = self.ticket_info.get("sleeper_preference", "下铺")
        # window_seat = self.ticket_info.get("window_seat", True)
        # 先筛选车次
        if preferred_trains:
            preferred_trains_set = set(preferred_trains)
            tickets = [t for t in tickets if any(trains in t for trains in preferred_trains_set)and from_station_code in t]
        tickets = self.Filtered_tickets(tickets)
        # 步骤2：再筛选出含有配置中座位类型的，并且这些类型有票的
        def has_configured_seat_with_ticket(ticket):
            for seat in seat_priority:
                val = ticket.get(seat, '--')
                if val not in ['--', '', None]:
                    return True
            return False
        filtered = [t for t in tickets if has_configured_seat_with_ticket(t)]
        '''# 步骤3：根据座位优先级排序
        def seat_score(ticket):
            for i, seat in enumerate(seat_priority):
                val = ticket.get(seat, '--')
                if val not in ['--', '无', '', None]:
                    return i
            return len(seat_priority) + 1

        filtered.sort(key=seat_score)
        print(f'第三次筛选出{len(filtered)}趟车次')
        # print(filtered)'''
        if len(filtered) == 0:
            logger.error(f"共有{len(filtered)}辆车符合条件 车号错了还是座位错了？")
            logger.error("程序退出")
            exit()
        return filtered #车票信息已进行切割和筛选 返回的是列表包含字典[{}]
    def Filtered_tickets(self,tickets: list[dict]) -> list[dict]:
        # 定义座位索引和名称的映射
        all_train_result = []
        for ticket in tickets:
            parts = ticket.split('|')
            train_info = {
                'train_no': parts[2],
                'stationTrainCode': parts[3],
                'from_station_code':parts[6],
                'to_station_code': parts[7],
                'start_time': parts[8],
                'arrive_time': parts[9],
                'duration': parts[10],
                'can_book' : parts[11],
                '商务座': parts[32] or '--',
                '一等座': parts[31] or '--',
                '二等座': parts[30] or '--',
                '硬卧': parts[28] or '--',
                '软卧': parts[23] or '--',
                '硬座': parts[29] or '--',
                '无座': parts[26] or '--',
                'secretStr': urllib.parse.unquote(parts[0]),
                '所有的座位类型': parts[34],
                '有票的座位类型': parts[35],
                'bed_level_info': parts[53],
            }
            all_train_result.append(train_info)
        return all_train_result
