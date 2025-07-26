
import time
from datetime import datetime

# === ⏳ 等待到指定时间（比如晚上 22:30:00） ===
target_time_str = "01:48:00"
target_time = datetime.strptime(target_time_str, "%H:%M:%S")
print(f"⏳ 等待时间点：{target_time_str}")
print(type(target_time))
while True:
    now = datetime.now().time()
    if now >= target_time.time():
        print(type(target_time.time()))
        print(f"⏰ 到达指定时间：{now}，开始后半部分")
        break
    time.sleep(1)


from datetime import datetime, timedelta

target = datetime.strptime("01:00:00", "%H:%M:%S")
start = target - timedelta(minutes=3)
print(f"⏳ 等待时间点：{target}")
while True:
    now = datetime.now()
    if now.time() >= start.time():
        print("可以开始运行")
        break
    time.sleep(1)
