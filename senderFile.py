#!/usr/bin/env python

from socket import *
import sys,time

s = socket(AF_INET,SOCK_DGRAM)
host = '10.20.1.8'
port = 8000
buf =20480
file_name=sys.argv[1]

s.sendto((file_name).encode(),(host,port))

f=open(file_name,"rb")
data = f.read(buf)
while (data):
    if(s.sendto(data,(host,port))):
        print("sending ...")
        data = f.read(buf)
    #time.sleep(0.1)
s.close()
f.close()