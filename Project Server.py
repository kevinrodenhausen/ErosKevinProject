# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:41:39 2019

@author: erosg
"""

from threading import Thread
from socket import *
#import time
import sys
#import fileinput
import os 

def processRequest(connectionSocket, addr):
    try:
        message = connectionSocket.recv(1024)
        path = "C:/Users/erosg/OneDrive/Desktop/" # Can be changed if need be
        
        dirName = message.split()[1]
        # message.split() == [b'GET', b'/test.html', b'HTTP/1.1', b'Host:', 
        # b'10.12.75.200:12000', b'Connection:', b'keep-alive', 
        # b'Cache-Control:', b'max-age=0', b'Upgrade-Insecure-Requests:', 
        # b'1', b'User-Agent:', b'Mozilla/5.0', b'(Linux;', b'Android', 
        # b'7.0;', b'LG-M327)', b'AppleWebKit/537.36', b'(KHTML,', b'like', 
        # b'Gecko)', b'Chrome/73.0.3683.90', b'Mobile', b'Safari/537.36', 
        # b'DNT:', b'1', b'Accept:', b'text/html,application/xhtml+xml,
        # application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,
        # application/signed-exchange;v=b3', b'Accept-Encoding:', b'gzip,', 
        # b'deflate', b'Accept-Language:', b'en-US,en;q=0.9']
        
        dirName = dirName[1:].decode("utf-8")
        # dirName[1:] == "test"
        
        path = path + dirName + "/"
        
        #print(path)
        
        for filename in os.listdir(path):
            print(filename)
            f = open(filename)
            outputdata = f.read()
            # output == all characters in html file
            
            connectionSocket.send(("HTTP/1.1 200 OK\r\n\r\n").encode())
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
        
    except IOError:
        connectionSocket.send(("HTTP/1.1 404 Not Found\r\n\r\n").encode())
    finally:
        connectionSocket.close()

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(5)

while True:
    print("The server is ready to receive")
    connectionSocket, addr = serverSocket.accept()
    t = Thread(target = processRequest, args = (connectionSocket, addr))
    t.start()
    
serverSocket.close()
sys.exit()