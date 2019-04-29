# python 多线程测试v2

import threading
from threading import current_thread;


class MyThread(threading.Thread):
    def run(self):
        print(current_thread().getName(), 'start')
        print('run!')
        print(current_thread().getName(), 'end')


test1 = MyThread()
test1.start()
test1.join()

test2 = MyThread()
test2.start()