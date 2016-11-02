#!/usr/bin/python3.5
from socket import *

addr = (gethostbyaddr("127.0.0.1"), 4711)
buf = 128

UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)

while True:
    data, addr = UDPSock.recvfrom(buf)
    if data:
        print("Client: ", addr, " Nachricht: ", data)
        UDPSock.sendto("Hallo Client!", addr)
    else:
        break

UDPSock.close()
