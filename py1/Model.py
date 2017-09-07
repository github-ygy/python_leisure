#!/usr/bin/env python
# author：ygy

import sys    ###导入模块

import os

import Grammar  ####可以导入当前目录下的其他模块


print(sys.path)
####python库
# ['F:\\pythonProjectHome\\python_leisure\\py1',
#  'F:\\pythonProjectHome\\python_leisure',
#  'C:\\Windows\\SYSTEM32\\python34.zip',
#  'C:\\Python34\\DLLs', 'C:\\Python34\\lib',
#  'C:\\Python34',
#  'C:\\Python34\\lib\\site-packages']

print(sys.argv)  ###对比为java中 String [] args

os.system("dir")
command = os.popen("dir").read()

print(command)

#os.mkdir("new dir") ###会在当前目录创建new dir 目录






