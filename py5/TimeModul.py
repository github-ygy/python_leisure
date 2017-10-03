#!/usr/bin/env python
# author：ygy


import time

#时间戳
# print(time.time())
#不传入参数显示默认的当前时间
# print(time.gmtime())  #utc时区
# print(time.localtime()) #本地时区 utc+8 时区
# 传入参数 秒数，显示指定时间
# print(time.localtime(time.time()))

local_time = time.localtime()
#取出年 月 日
print(local_time)
print(local_time.tm_year)
print(local_time.tm_mon)
print(local_time.tm_mday)

#将时间转化为时间戳
seconds =time.mktime(local_time)
print(seconds)

##转化为指定格式的string
# help(time.strftime)
time_string = time.strftime("%Y-%m-%d %H:%M:%S",local_time)
print(time_string)
##将string按照指定格式转为时间
time_date = time.strptime(time_string,"%Y-%m-%d %H:%M:%S")
print(time_date)