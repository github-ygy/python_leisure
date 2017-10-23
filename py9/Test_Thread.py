#!/usr/bin/env python
# author：ygy

import  threading
import time

#多线程实现方式1
def run (name):
    print("my name is %s"%name)
    time.sleep(2)
    print(" %s is done "%name)


t = threading.Thread(target=run,args=("ygy",))
t.setDaemon(True)
t.start()

# t.join()

print(" main is end ")