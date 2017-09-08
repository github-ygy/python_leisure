#!/usr/bin/env python
# author：ygy

####三元运算符号
#
# a,b,c = 1 ,3 ,5
#
# d = a if a < b else c
#
# print(d)

###数据类型  int（无long） float str boolean bytes

###bytes类型
str ="字符串"

print(str.encode("utf-8").decode("utf-8"))

###数据结构

##数组[]  与java  int []类似
ages = [22,32,57,32,346]
# print(ages[2])
# print(ages[2:3])  ##前闭后开
# print(ages.__sizeof__())
# ages.insert(1,27)   ##插入到指定位置
# print(ages)
print(ages[::2])  ###隔一个打印

for i in ages[::2]:
    print(i)

###删除
# ages.remove(32)
# del ages[0]
# ages.pop()  ###默认删除最后一位
# print(ages)

import copy

###浅copy
new_ages = copy.copy(ages)
##深copy
deep_copy = copy.deepcopy(ages)

print(new_ages)

for i in new_ages:
    print(i)

###元组  不可变列表,只能查询，不能修改
tupe_ages = (12,23,214)
print(tupe_ages)



