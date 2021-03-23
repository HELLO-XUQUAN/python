#!/usr/bin/python3

import socket
import time
import os

import re
pattern = re.compile(
    r'^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|'
    r'([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})|'
    r'([a-zA-Z0-9][-_.a-zA-Z0-9]{0,61}[a-zA-Z0-9]))\.'
    r'([a-zA-Z]{2,13}|[a-zA-Z0-9-]{2,30}.[a-zA-Z]{2,3})$'
)


def getIP(domain):
    myaddr = socket.getaddrinfo(domain, 'http')
    print( domain, myaddr[0][4][0])

if __name__ == '__main__':
    print("------begin------")
    with open('domain.txt','r') as f:
        for line in f.readlines():
            line = line.strip()
            if pattern.match(line):  #判断是否符合域名 格式
                getIP(line)
            else:
                print( line ,"not domain！！")
            
    print("---ping over!!---")
    
#add new
   print("new")
