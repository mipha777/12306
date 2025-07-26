import httpx
from collections import OrderedDict

headers = OrderedDict([
    ("Host", "kyfw.12306.cn"),
    ("Connection", "keep-alive"),
    ("Cache-Control", "max-age=0"),
    ("Upgrade-Insecure-Requests", "1"),
    ("User-Agent", "UA"),
    ("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"),
    ("Referer", "https://kyfw.12306.cn/otn/view/index.html"),
    ("Accept-Encoding", "gzip, deflate, br"),
    ("Accept-Language", "zh-CN,zh;q=0.9"),
    ("Cookie", "cookie")
])

with httpx.Client(http1=True) as client:
    r = client.get("https://httpbin.org/anything", headers=headers)
    print(r.text)
