#!/usr/bin/env python
# author：ygy

msg = " global "

##局部变量
def getName(name):
    age = 22
    print(" name :",name)
    print(" age :",age)


# getName("ygy")


#全局变量
def getMsg():
    # global msg
    # msg = " local "
    print(" msg : " ,msg)

getMsg()

print(msg)