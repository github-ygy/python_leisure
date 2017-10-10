#!/usr/bin/env python
# author：ygy



class Person(object):

    def __init__(self,name):
        self.name = name

    def talk(self):
        print(" %s is talking "%self.name)


    def eat(self,food):
        print("%s is eating %s"%(self.name,food))


p = Person("ygy")
# p.eat("rice")

input_str = input(">>>").strip()

# if hasattr(p,input_str):
#     method = getattr(p,input_str)   #反射获取属性，如果为方法，则获取为地址值
#     method()
# else:
#     print(" not this method")

#带参数的反射
# if hasattr(p,input_str):
#     method = getattr(p,input_str)   #反射获取属性，如果为方法，则获取为地址值
#     print(method)           #可以直接获取实例变量
    # method("meet ")


#设置反射属性       #本质是操作字符串，可以讲字符串与内存地址相互转化
setattr(p,input_str,"ygy's friend")

method = getattr(p,"talk")
method()
























