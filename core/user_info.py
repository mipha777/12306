# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/7/22 15:09
@Desc     : 获取和处理乘车人信息
"""

import yaml
from utils.logger import logger
from utils.clean_cookies import cookies_clean
# 证件类型映射（常用：1-二代身份证，C-港澳通行证，G-台湾通行证）
ID_TYPE_MAP = {
    '身份证': '1',
    '港澳通行证': 'C',
    '台湾通行证': 'G',
    '护照': 'B',
}

# 座位类型映射（常用：商务座9，一等座M，二等座O，软卧4，硬卧3，硬座1，无座1）
SEAT_TYPE_MAP = {
    '商务座': '9',
    '特等座': 'P',
    '一等座': 'M',
    '二等座': 'O',
    '高级软卧': '6',
    '软卧': '4',
    '硬卧': '3',
    '软座': '2',
    '硬座': '1',
    '无座': '1',
}
def build_passenger_strings(config, passengers ,response_json: dict):
    """
    根据配置文件和座位类型，拼接 passengerTicketStr 和 oldPassengerStr
    :param config_path: 配置文件路径
    :param 
    :return: (passengerTicketStr, oldPassengerStr)
    """
    passengers = passengers
    seat_type_name = config.get('ticket_info', {}).get('seat_priority')
    seat_type = SEAT_TYPE_MAP.get(seat_type_name[0]) # 座位类型
    all_info =  response_json["data"]["normal_passengers"]
    for passenger_info in all_info:
        if passenger_info['passenger_name'] == passengers:
            Ticket_type = '0' # 票类型 0 成人 1 儿童 2 学生 3 军人
            passenger_type = passenger_info["passenger_type"]  # 乘客类型 1 成人
            passenger_name = passenger_info["passenger_name"]  # 乘客姓名 
            passenger_id_type_code = passenger_info["passenger_id_type_code"]  # 证件类型 1
            passenger_id_no = passenger_info["passenger_id_no"]  # 乘客证件号码 411
            mobile_no = passenger_info["mobile_no"]  # 乘客手机号
            mysticalparameter = 'N'  # 不知名参数 默认为N
            allEncStr = passenger_info["allEncStr"]  # 加密字符串
            passengerTicketStr = f"{seat_type},{Ticket_type},{passenger_type},{passenger_name},{passenger_id_type_code},{passenger_id_no},{mobile_no},{mysticalparameter},{allEncStr}"
            oldPassengerStr = f"{passenger_name},{passenger_id_type_code},{passenger_id_no},1_"
            logger.info('核实预填乘车人成功')
            return passengerTicketStr, oldPassengerStr
        else:
            logger.info('核实预填乘车人信息中...')
    logger.error('手机上并未添加乘车人信息认证')
    logger.info('即将清除使用信息 并退出程序')
    cookies_clean()
    logger.info('程序退出')
if __name__ == '__main__':
    
    import os

    # 当前文件的目录
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # config.yaml 所在目录 = 当前目录的上一级
    parent_dir = os.path.dirname(current_dir)

    # 拼接出 config.yaml 的绝对路径
    config_path = os.path.join(parent_dir, 'config.yaml')

    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    build_passenger_strings(config, data)
    # p_str, op_str = build_passenger_strings(config, data)
    # print(p_str)
    # print(op_str)