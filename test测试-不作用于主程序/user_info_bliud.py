# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/7/26 00:02
@Desc     : 
"""

seat_type = '3'
Ticket_type = '0'  # 票类型 0 成人 1 儿童 2 学生 3 军人
passenger_type = '1'  # 乘客类型 1 成人
passenger_name = '李浩歌'  # 乘客姓名 zsl
passenger_id_type_code = '1'  # 证件类型 1
passenger_id_no = '4127***********634'  # 乘客证件号码 411
mobile_no = '188****2698'  # 乘客手机号
mysticalparameter = 'N'  # 不知名参数 默认为N
allEncStr = "1be6b8b1e436f0de43998e478148524d20ac2bc947d2b58d3218a4b10eae8f4efc0cf22e751e14cedeb261b42fb95c637064a5591b72b58314cebc71cdf405e1dee4af3f0947645264e03dea190d5e32"  # 加密字符串
passengerTicketStr = f"{seat_type},{Ticket_type},{passenger_type},{passenger_name},{passenger_id_type_code},{passenger_id_no},{mobile_no},{mysticalparameter},{allEncStr}"
oldPassengerStr = f"{passenger_name},{passenger_id_type_code},{passenger_id_no},1_"
'''
"passenger_name": "李浩歌",
        "sex_code": "M",
        "sex_name": "男",
        "born_date": "2001-08-29 00:00:00",
        "country_code": "CHN",
        "passenger_id_type_code": "1",
        "passenger_id_type_name": "居民身份证",
        "passenger_id_no": "4127***********634",
        "passenger_type": "1",
        "passenger_type_name": "成人",
        "mobile_no": "188****2698",
        "phone_no": "",
        "email": "",
        "address": "",
        "postalcode": "",
        "first_letter": "LHG",
        "recordCount": "4",
        "isUserSelf": "N",
        "total_times": "99",
        "index_id": "2",
        "allEncStr": "1be6b8b1e436f0de43998e478148524d20ac2bc947d2b58d3218a4b10eae8f4efc0cf22e751e14cedeb261b42fb95c637064a5591b72b58314cebc71cdf405e1dee4af3f0947645264e03dea190d5e32",'''
print(passengerTicketStr)
print(oldPassengerStr)
print(type(passengerTicketStr))