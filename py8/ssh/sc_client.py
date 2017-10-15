#!/usr/bin/env python
# author：ygy


import socket




sc = socket.socket()
sc.connect(("localhost",9999))


while True:
    command =  input(">>>>").strip()

    sc.send(command.encode())

    resp_len = sc.recv(1024)
    print(" resp_len :",resp_len.decode())
    receive_sise = 0
    receive_data = b""
    while receive_sise < int(resp_len.decode()):
        data = sc.recv(1024)
        receive_sise+=len(data)
        receive_data+=data
    else:
        print("receive size :",receive_sise)
        print(" receive data :",receive_data.decode())

sc.close()
