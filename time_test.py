# 时间类库
import time
import datetime

import random

print(time.time())
print(time.localtime().tm_hour)
print(time.strftime("%Y-%m-%d %H:%M:%S"))

print(datetime.datetime.now())

plus_time = datetime.timedelta(days=1)

print(datetime.datetime.now() - plus_time)

print(random.randint(1, 100))

print(random.choice(['aaa', 'bbb', 'ccc']))