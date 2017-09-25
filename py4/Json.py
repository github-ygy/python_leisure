#!/usr/bin/env python
# author：ygy

import json


file = open("test",'w',encoding="utf-8") #文件句柄 写读

#定义一个字典
info = {
    "name":"ygy",
    "age":22
}
file.write( json.dumps(info))
file.close()

read_file = open("test.txt","r")

for line in read_file:
    print(line)

msg = json.loads(file.readline())
print(msg["age"])

read_file.close()







