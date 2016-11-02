#!/usr/bin/python3.5

from socket import *

addr = (gethostbyaddr("127.0.0.1"), 4711)
buf = 128

UDPSock = socket(AF_INET, SOCK_DGRAM)
data = "Hallo Server!"

UDPSock.sendto(data, addr)
(data, addr) = UDPSock.recvfrom(buf)

print("Server: ", addr, " Nachricht:", data)
UDPSock.close()
