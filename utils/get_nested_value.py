# 进行配置文件内容的检查
import os
import json
# 获取当前文件所在目录（即 utils/）
cur_dir = os.path.dirname(__file__)

# 拼出目标 JSON 文件路径：跳出一层到项目根，再进 data 文件夹
json_path = os.path.join(cur_dir, '..', 'data', 'station_name_map.json')
json_path = os.path.abspath(json_path)

def get_nested_value_fun(data: dict, key_path: str):
    """
    从配置文件中提取值
    """
    keys = key_path.split('.')
    for key in keys:
        if isinstance(data, dict) and key in data:
            data = data[key]
        else:
            return None
    return data


def get_station_codes(from_station, to_station):
    with open(json_path, 'r', encoding='utf-8') as f:
        station_dict = json.load(f)

    from_code = station_dict.get(from_station)
    to_code = station_dict.get(to_station)
    
    if not from_code or not to_code:
        raise ValueError(f"找不到车站代码: {from_station if not from_code else ''} {to_station if not to_code else ''}")
    return from_code, to_code