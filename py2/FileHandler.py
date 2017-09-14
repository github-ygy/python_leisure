#!/usr/bin/env python
# author：ygy

#file = open("test",'r+',encoding="utf-8") #文件句柄 读写
#file = open("test",'w+',encoding="utf-8") #文件句柄 写读
#file = open("test",'a+',encoding="utf-8") #文件句柄 追加读写
#file = open("test",'rb') #文件句柄 字节类型
####写文件时为先创建文件
# file = open("test",encoding="utf-8")
# file.write(" \n this is append data\n")
# data = file.read()
# print(" data =  ",data)

##迭代器打印
# for line in file:
#     print(line.strip())
#
# print(file.tell())   ##文件指针 起始0
# print(len(file.readline()))
# print(file.tell())   ### file.readline().strip().length
# file.seek(10)  ##跳到指定指针位置
# print(file.tell())
#
# file.close() ##关闭资源

## 修改文件
# file = open("test","r",encoding= "utf-8")
# new_file = open("new_test","w",encoding="utf-8")
##自动关闭
with open("test", "r", encoding="utf-8") as file, open("new_test","w",encoding="utf-8") as new_file:
    for line in file:
        if "append" in line:
            line = line.replace("append","new word",-1)
        new_file.write(line)
# file.close()
# new_file.close()




