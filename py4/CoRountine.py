#!/usr/bin/env python
# author：ygy



###协程

def consumer(name):
    print(" %s 要开始预订票了"%(name))
    while True:
        ticket = yield
        print( "%s 预订到了 票号为： %s" %(name,ticket))

def producer():
    consu1 = consumer("ygy")
    consu2 = consumer("lc")
    next(consu1)   ### 阻塞在 yield
    next(consu2)   ### 阻塞在 yield
    for i in range(10):
       if(i % 2 == 0):
           consu1.send(i)   #返回到consumer函数的yield 继续执行
       else:
           consu2.send(i)


# gen = consumer(" ygy ")
# next(gen)
# gen_num = 1
# gen.send(gen_num)


producer()


