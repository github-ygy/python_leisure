#!/usr/bin/env python
# author：ygy


import threading, time


def run(n):
    semaphore.acquire()  #信号量计数
    print("run the thread: %s" % n)
    time.sleep(1)
    print("off the thread:%s" % n)
    semaphore.release()   #释放数量


# if __name__ == '__main__':
semaphore = threading.BoundedSemaphore(5)  # 最多允许5个线程同时运行
for i in range(22):
    t = threading.Thread(target=run, args=(i,))
    t.start()
