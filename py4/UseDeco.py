#!/usr/bin/env python
# author：ygy


import time

#使用高阶函数与嵌套函数实现装饰者模式
# def calTime(func):
#     def decoFunc():
#         startTime = time.time()
#         func()
#         endTime = time.time()
#         print(" func takes time = %s" %(endTime - startTime))
#     return  decoFunc
#
# def test():
#     time.sleep(3)
#     print(" test is end ")
#
# test = calTime(test)  #传递函数地址
# test()


##python 实现装饰者模式
def calTime(func):
    def decoFunc(*args,**kwargs):
        startTime = time.time()
        func(*args,**kwargs)
        endTime = time.time()
        print(" func takes time = %s" %(endTime - startTime))
    return  decoFunc

@calTime
def test(msg):
    time.sleep(3)
    print(" test is end " + msg)

test(msg="this is extra param ")












