#!/usr/bin/env python

from socket import *
import sys,traceback,select

host="10.20.1.8"
port = 8000
s = socket(AF_INET,SOCK_DGRAM)
s.bind((host,port))

addr = (host,port)
buf=20480

data,addr = s.recvfrom(buf)
print ("Received File:",data.strip())
f = open("pruba-copy.pdf",'wb')

data,addr = s.recvfrom(buf)
try:
    while(data):
        print(data)
        f.write(data)
        s.settimeout(2)
        data,addr = s.recvfrom(buf)
except timeout:
    traceback.print_exc(file=sys.stdout)
    f.close()
    s.close()
    print ("File Downloaded")