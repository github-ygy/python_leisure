#!/usr/bin/env python
# author：ygy


import  queue,threading,time

def producer():
    count = 1
    while True:
        print("生产了票-%s"%count)
        ticketQueue.put(" 票-%s"%count)
        count+=1
        time.sleep(0.5)


def consumer(name):
    while True:
        print("%s,购买了%s"%(name,ticketQueue.get()))
        time.sleep(1)

ticketQueue = queue.Queue(maxsize=20)


pro = threading.Thread(target=producer,args=())
cons1 = threading.Thread(target=consumer,args=("ygy---",))
cons2 = threading.Thread(target=consumer,args=("yebuhei---",))

pro.start()
cons1.start()
cons2.start()



