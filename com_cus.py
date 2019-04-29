# 生产者消费者模型

import random
import time
from queue import Queue
from threading import Thread
from threading import current_thread
from threading import Lock

queue = Queue(5)


# 生产者
class ProducerThread(Thread):
    def run(self):
        name = current_thread().getName()
        nums = range(100)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print('生产者 producer-%s 生产了数据 %s' % (name, num))
            rand_t = random.randint(1, 3)
            time.sleep(rand_t)
            print('生产者 producer-%s 休眠了 %s' % (name, rand_t))


# 消费者
class ConsumerThread(Thread):
    def __init__(self, name):
        super().__init__()
        self._lock = Lock()  # 锁可以锁住部分代码块
        self.name = name

    def run(self):
        name = current_thread().getName()
        global queue
        while True:
            # self._lock.acquire()
            num = queue.get()
            queue.task_done()
            # self._lock.release()
            print('消费者 consumer-%s 消费了 %s' % (name, num))
            rand_t = random.randint(1, 3)
            time.sleep(rand_t)
            print('消费者 consumer-%s 休眠了 %s' % (name, rand_t))


producer_thread = ProducerThread(name='producer_thread1')
producer_thread.start()

consumer_thread = ConsumerThread(name='consumer_thread1')
consumer_thread.start()

consumer_thread2 = ConsumerThread(name='consumer_thread2')
consumer_thread2 .start()