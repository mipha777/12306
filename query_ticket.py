# -*- coding: utf-8 -*-
"""
@Desc: 查票功能测试入口（集成查询逻辑）
"""
import yaml
import json
import urllib.parse
from core.session_manager import SessionManager
from utils.headers_utils import build_dynamic_headers

# --- 将 TicketQuerier 的逻辑直接集成到这里 ---

# 查票接口 URL
QUERY_URL = "https://kyfw.12306.cn/otn/leftTicket/query"

def query_tickets(session_manager: SessionManager, from_station_name: str, to_station_name: str, train_date: str):
    """
    执行一次查票请求
    """
    # 1. 加载车站映射
    try:
        with open("data/station_name_map.json", 'r', encoding='utf-8') as f:
            station_map = json.load(f)
    except Exception as e:
        print(f"加载车站映射文件失败: {e}")
        return None

    # 2. 获取车站代码
    from_station_code = station_map.get(from_station_name)
    to_station_code = station_map.get(to_station_name)
    if not all([from_station_code, to_station_code]):
        print(f"出发站({from_station_name})或到达站({to_station_name})不存在于映射文件中。")
        return None

    # 3. 更新查询 Cookie
    from_cookie_val = f"{urllib.parse.quote(from_station_name)},{from_station_code}"
    to_cookie_val = f"{urllib.parse.quote(to_station_name)},{to_station_code}"
    # 假设 session_manager 中有 update_query_cookies 方法
    if hasattr(session_manager, 'update_query_cookies'):
        session_manager.update_query_cookies(from_cookie_val, to_cookie_val, train_date)
    else:
        print("W: SessionManager 中缺少 update_query_cookies 方法，部分 cookie 可能未更新。")


    # 4. 构建请求参数和请求头
    params = {
        "leftTicketDTO.train_date": train_date,
        "leftTicketDTO.from_station": from_station_code,
        "leftTicketDTO.to_station": to_station_code,
        "purpose_codes": "ADULT"
    }
    referer_url = (f"https://kyfw.12306.cn/otn/leftTicket/init?"
                   f"linktypeid=dc&fs={from_cookie_val}&ts={to_cookie_val}&date={train_date}&flag=N,N,Y")

    headers = build_dynamic_headers({
        "Referer": referer_url,
        # 其它接口需要的头部
    })

    # 5. 发起请求
    try:
        print(f"正在查询 {train_date} 从 {from_station_name} 到 {to_station_name} 的车票...")
        resp = session_manager.get_session().get(QUERY_URL, params=params, headers=headers, timeout=10)
        resp.raise_for_status()
        result = resp.json()
        if result.get("status"):
            print("查询成功！")
            return result.get("data", {})
        else:
            print(f"查询失败: {result.get('messages')}")
            return None
    except Exception as e:
        print(f"请求查票接口时发生错误: {e}")
        return None

def run_query():
    """执行查票流程"""
    try:
        with open("config.yaml", 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        user_config = config.get("user", {})
        ticket_config = config.get("ticket_info", {})
        username = user_config.get("username")
        from_station = ticket_config.get("from_station")
        to_station = ticket_config.get("to_station")
        train_date = ticket_config.get("train_date")

        if not all([username, from_station, to_station, train_date]):
            print("config.yaml 中的用户或票务信息不完整。")
            return
    except Exception as e:
        print(f"加载配置文件时出错: {e}")
        return

    session_manager = SessionManager(username)
    if not session_manager.load_cookies():
        print("未找到有效的 cookie，请先运行 login.py 登录。")
        return

    query_result = query_tickets(session_manager, from_station, to_station, train_date)

    if query_result:
        print("查询结果分析：")
        result_list = query_result.get('result', [])
        station_names = query_result.get('map', {})
        if not result_list:
            print("   -> 未查询到符合条件的车次。")
            return

        print(f"共查询到 {len(result_list)} 趟列车。")

        # 定义座位索引和名称的映射
        seat_map = {
            3: '车次',8: '出发时间',9: '到达时间',10: '历时',11: '能否预定',32: '商务座/特等座',31: '一等座',30: '二等座',
            29: '硬座',28: '硬卧/二等卧',27: '软座',26: '无座',25: '其他',23: '软卧/动卧/一等卧',21: '高级软卧',20: '优选一等座'
        }

        # 打印表头
        header = (f"{'车次':<5} | {'出发':<10} -> {'到达':<11} | {'历时':<4} | "
                  f"{'状态':<5} | {'商务座':<5} | {'一等座':<5} | {'二等座':<5} | "
                  f"{'软卧':<5} | {'硬卧':<5} | {'硬座':<5} | {'无座':<5}")
        print("-" * len(header))
        print(header)
        print("-" * len(header))

        for item in result_list:
            parts = item.split('|')

            # 基本信息
            train_no = parts[3]
            from_station_code = parts[6]
            to_station_code = parts[7]
            start_time = parts[8]
            arrive_time = parts[9]
            duration = parts[10]
            can_book = parts[11] == 'Y'
            # 这里的 status 是服务器返回的原始状态，如 "预订"
            status = parts[1]

            from_station_name = station_names.get(from_station_code, from_station_code)
            to_station_name = station_names.get(to_station_code, to_station_code)

            # 如果不能预订，状态信息可能在别处
            status_text = status if can_book else parts[0].split(';')[0] if '|' not in parts[0] else status
            if "列车停运" in status_text:
                status_text = "停运"

            # 票量信息
            tickets_info = {}
            for index, seat_name in seat_map.items():
                ticket_count = parts[index] if parts[index] else "--"
                tickets_info[seat_name] = ticket_count

            print(
                f"{train_no:<6} | {from_station_name}({start_time}) -> {to_station_name}({arrive_time}) | "
                f"{duration:<6} | {status_text:<5} | "
                f"{tickets_info.get('商务座', '--'):<6} | "
                f"{tickets_info.get('一等座', '--'):<6} | "
                f"{tickets_info.get('二等座', '--'):<6} | "
                f"{tickets_info.get('软卧', '--'):<6} | "
                f"{tickets_info.get('硬卧', '--'):<6} | "
                f"{tickets_info.get('硬座', '--'):<6} | "
                f"{tickets_info.get('无座', '--'):<5}"
            )

if __name__ == '__main__':
    run_query()
