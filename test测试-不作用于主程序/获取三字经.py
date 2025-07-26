# -*- coding: utf-8 -*-
"""
@Author   : shaozi
@Version  : Python 3.12
@Date     : 2025/7/23 15:12
@Desc     : 
"""
import re
import json
import requests

def fetch_station_codes(output_path='12306_stations.json'):
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js'
    headers = {'User-Agent': 'Mozilla/5.0'}
    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()

    # 提取单引号中的所有车站数据
    text = resp.text
    m = re.search(r"station_names\s*=\s*'(.+)';", text)
    data = m.group(1) if m else ''

    stations = {}
    for seg in data.split('@'):
        if not seg: continue
        parts = seg.split('|')
        # parts: [abbr, stationName, stationCode, pinyin, ...]
        stations[parts[1]] = parts[2]

    # 保存为 JSON
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(stations, f, ensure_ascii=False, indent=2)

    print(f"✅ 已保存 {len(stations)} 个车站三字码到 {output_path}")
    return stations

if __name__ == '__main__':
    fetch_station_codes()
