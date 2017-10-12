#!/usr/bin/env python
# author：ygy

import socket



sc = socket.socket()

#将套接字绑定到地址。address地址的格式取决于地址族。在AF_INET下，以元组（host,port）的形式表示地址
sc.bind(("localhost",8888))
#开始监听传入连接。backlog指定在拒绝连接之前，可以挂起的最大连接数量。
sc.listen(5)

while True:
    conc, addr = sc.accept()  ##阻塞获取连接信息 和 地址
    while True:
        print(" conc :",conc,"  - addr:",addr)
        data = conc.recv(1024)
        if not data:
            print(" clint is lost ")
            break
        print(data.decode())
        conc.send(data.decode().upper().encode())
sc.close()