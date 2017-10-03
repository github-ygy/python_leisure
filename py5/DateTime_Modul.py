#!/usr/bin/env python
# author：ygy

import datetime

#获取当前时间

now_time = datetime.datetime.now()
print(now_time) #2017-10-04 00:03:11.710409

#获取过去前3天的时间
print(now_time+datetime.timedelta(-3))
#3小时前
print(now_time+datetime.timedelta(hours=-3))
#3分钟前
print(now_time+datetime.timedelta(minutes=-3))
