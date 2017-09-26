#!/usr/bin/env python
# author：ygy



## 导入Test 模块
#模块： .py文件
#导入模块：解释python文件
#导入包：解释init文件

#导入模块
# import  Test
#
# Test.test()
# print(Test.age)

#导入包



#导入包下的其它文件

#导入的实质是查找sys.path下的文件路径搜索


import sys,os

print(sys.path)   #路径列表



abs_path = os.path.abspath(__file__)

print(abs_path)  #该文件下的绝对路径

abs_dir = os.path.dirname(abs_path)  #获取父目录

print(abs_dir)

base_dir = os.path.dirname(abs_dir)

print(base_dir)

sys.path.append(base_dir)   #将base目录添加到sys.path 路径下

import ImportTest


ImportTest.logging()
ImportTest.helloworld()
print(ImportTest.name)

