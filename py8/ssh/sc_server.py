#!/usr/bin/env python
# author：ygy


import socket,os

sc =  socket.socket()
sc.bind(("localhost",9999))
sc.listen(5)


while True:
    conn,addr =  sc.accept();
    while True:
        commandByte = conn.recv(1024)
        if not commandByte:
            break  #客户端断开
        print("command :",commandByte.decode())
        command_resp = os.popen(commandByte.decode()).read()

        if(len(command_resp) == 0):      #如果发送数据的长度为0会被阻塞
            command_resp = " this is invalid command"
        conn.send(str(len(command_resp.encode())).encode())
        conn.send(command_resp.encode())

sc.close()
