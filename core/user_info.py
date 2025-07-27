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
            passenger_name = passenger_info["passenger_name"]  # 乘客姓名 zsl
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
    data = {
        "validateMessagesShowId": "_validatorMessage",
        "status": 'true',
        "httpstatus": 200,
        "data": {
            "notify_for_gat": "",
            "isExist": 'true',
            "exMsg": "",
            "two_isOpenClick": [
            "93",
            "95",
            "97",
            "99"
            ],
            "other_isOpenClick": [
            "91",
            "93",
            "98",
            "99",
            "95",
            "97"
            ],
            "normal_passengers": [
            {
                "passenger_name": "张森林",
                "sex_code": "M",
                "sex_name": "男",
                "born_date": "2001-10-04 00:00:00",
                "country_code": "CHN",
                "passenger_id_type_code": "1",
                "passenger_id_type_name": "居民身份证",
                "passenger_id_no": "4116***********912",
                "passenger_type": "1",
                "passenger_type_name": "成人",
                "mobile_no": "166****0702",
                "phone_no": "",
                "email": "",
                "address": "",
                "postalcode": "",
                "first_letter": "ZSL",
                "recordCount": "6",
                "isUserSelf": "Y",
                "total_times": "99",
                "index_id": "0",
                "allEncStr": "432d99286ad3262483d7d67c6335504908695b23dd16a9d39fd82c738103fd052b7bbf790f19f30fc2d3d20146ca5eb58e465ae00e8efb8ab5e2af902cdb0931dee4af3f0947645264e03dea190d5e32",
                "isAdult": "Y",
                "isYongThan10": "N",
                "isYongThan14": "N",
                "isOldThan60": "N",
                "if_receive": "Y",
                "is_active": "N",
                "is_buy_ticket": "N",
                "last_time": "20210402222143",
                "passenger_uuid": "79fc3d73150eedd7e596ac3923ad158410daa34708d156ad37b83cc12aac47f2",
                "if_preferential": "",
                "mobile_code": "86",
                "temporay_age60": "N",
                "gat_born_date": "20011004",
                "gat_valid_date_start": "",
                "gat_valid_date_end": "",
                "gat_version": ""
            },
            {
                "passenger_name": "陈艳",
                "sex_code": "F",
                "sex_name": "女",
                "born_date": "2005-08-25 00:00:00",
                "country_code": "CHN",
                "passenger_id_type_code": "1",
                "passenger_id_type_name": "居民身份证",
                "passenger_id_no": "6107***********741",
                "passenger_type": "1",
                "passenger_type_name": "成人",
                "mobile_no": "166****0702",
                "phone_no": "",
                "email": "",
                "address": "",
                "postalcode": "",
                "first_letter": "CY",
                "recordCount": "6",
                "isUserSelf": "N",
                "total_times": "99",
                "index_id": "1",
                "allEncStr": "7c79e1a32dcac6de84c87723ccb7074dd2fa35cf73ba31c6947cfbc57cef84419746027a132f8e0dbecc46a91df2a6435571e48f893c05ee82dcfc77a57be75c821b7ff07379bad0bfe041e3ea1aeddf",
                "isAdult": "Y",
                "isYongThan10": "N",
                "isYongThan14": "N",
                "isOldThan60": "N",
                "if_receive": "Y",
                "is_active": "N",
                "is_buy_ticket": "N",
                "last_time": "20230915024624",
                "passenger_uuid": "55c3d90e41f00ad533a8840751a7cef0b6599a93e6c6c8df3b320bfd14be210c",
                "if_preferential": "",
                "mobile_code": "86",
                "temporay_age60": "N",
                "gat_born_date": "20050825",
                "gat_valid_date_start": "",
                "gat_valid_date_end": "",
                "gat_version": ""
            }
            ],
            "dj_passengers": []
        },
        "messages": [],
        "validateMessages": {}
}
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