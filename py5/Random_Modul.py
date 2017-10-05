#!/usr/bin/env python
# author：ygy


import random

print(random.random())   #0 - 1 的浮点数

print(random.randint(1,2)) # a - b 的int整数区间  前闭后闭

print(random.randrange(1,2))  # a - b 的int整数区间 前闭后开


##test
##大写字母和数字混合的验证码

checkCode = ''
for i in range(4):
    if(i % 2 == 0 ):
        checkCode += chr(random.randint(65,90))
    else:
        checkCode += str(random.randint(0,9))
print(checkCode)



