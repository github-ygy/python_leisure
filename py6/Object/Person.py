#!/usr/bin/env python
# author：ygy


class Person:

    #类变量
    state = "人"

    ##构造方法
    def __init__(self,name,age):
        self.name = name     #成员变量
        self.age = age

    #析构方法
    #当对象销毁，或者释放时调用
    def __del__(self):
        print(" %s self is destory" %self.name)


    def printDesc(self):
        print(" name = %s , age = %d"%(self.name,self.age))

#继承
class Man(Person):


    def __init__(self,name,age,desc):
        # Person.__init__(self,name,age)
        super(Man,self).__init__(name,age)
        self.desc = desc


    def printDesc(self):
        print(" this is man desc ")

# p1 = Person("ygy",22)
# p2 = Person("anoy",21)
#
# p1.printDesc()
#
# del p1    #销毁p1对象，调用析构方法
#
# p2.printDesc()
#
# print(p2.state)

m1 = Man("man",30,"this is man")
m1.printDesc()