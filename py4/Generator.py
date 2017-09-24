#!/usr/bin/env python
# author：ygy



##列表生成，直接全部加在到内存中，可以直接使用
# print([ i*2 for i in range (10)])

##换成() 则为生成器，只能一个个生成后调用

# generator = (i*2 for i in range(10)) ##是一个对象，不占内存，使用后才会初始化占用内存
# print(generator)  #<generator object <genexpr> at 0x0000000003698C18>
# # for i in  generator:
# #     print(i)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))


##斐波那契额数列 1  1 2 3 5 8 13 21

def func(count):
    n,a,b = 1 , 0, 1
    while(n<count):
        yield b     ##指定为生成器，每次都会获取b的值
        print(b,"aaaaaaaa")
        a,b = b,a+b   ##实际为 元组t =（b，a+b） a =t[0] b =t[1]
        n = n + 1
        # print(a)
        # yield a   ##指定为生成器
    return "异常的时候会被打印的消息"


# print(func(3))

gen = func(10)
for i in gen:  #返回到consumer函数执行，直到yield，获取当前b的值，在本函数中打印，
    print(i)




