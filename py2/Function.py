#!/usr/bin/env python
# author：ygy




#声明函数
# def func1():
#     print("　test func1 ")
#
# def func2():
#     print("　test func1 ")
#
# #调用函数
# func1()
# func2()

#返回值的函数
# def getFile():
#     return open("new_test",'a',encoding="utf-8")
#
# f = getFile()
# f.write(" haha \n")
# f.close()

#有参数的函数
# def sum(num1,num2):
#     return num1 + num2
#
# # print(sum(1,2))
# print(sum(num1=1,num2=2))


#传入多个参数
# def mulParam(*args):
#     print(args)
#
# mulParam(1,2,3,4,5,6)

#传入字典 key value形式
def mapParam(**kwargs):
    print(kwargs)

# mapParam(name="ygy",age='24')
mapParam(**{'name':'ygy','age':24})



