#!/usr/bin/env python
# author：ygy


import shutil

##copy  A文件 -->>> B文件
# fsrc = open("test","r",encoding="utf-8")
# fdst = open("test_copy","w",encoding="utf-8")
#
# shutil.copyfileobj(fsrc,fdst)  #默认length
#
# fsrc.close()
# fdst.close()

#拷贝文件  a 文件名 -》 B文件名
# shutil.copyfile("test","test_new_copy")

#拷贝文件及文件权限
shutil.copy("test", "test_stat_copy")























