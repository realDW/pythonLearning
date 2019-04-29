# python多线程

import threading
from threading import current_thread
import time

# 定义一个thread方法


def my_thread(arg1, arg2):
    time.sleep(2)
    print('%s %s %s' % (current_thread().getName(), arg1, arg2))


for i in range(1, 10, 1):
    test1 = threading.Thread(target=my_thread, args=('daiwei', 'hello'))
    test1.start()


print("thread test end!")