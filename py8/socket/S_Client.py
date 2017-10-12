#!/usr/bin/env python
# author：ygy


import  socket


#建立服务端连接

sc = socket.socket()
sc.connect(("localhost",8888))

#小写变大写服务
while True:
    word  = input(">>>>")
    sc.send(word.encode() ) #发送信息
    data = sc.recv(1024) #设置接收buff大小
    print(data.decode())
    if(data.decode() == "Q"):
        break

sc.close()  #关闭资源