# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 01:04:08 2019

@author: erosg
"""

import socket  
from socket import *   
import os

port = 50000
serverSocket = socket(AF_INET, SOCK_STREAM)
host = "" # Use localhost
serverSocket.bind((host, port))            
serverSocket.listen(5)
print("Server ready to connect....")

while True:
    conn, addr = serverSocket.accept()     # Establish connection with client.
    print('Got connection from', addr)
    data = conn.recv(1024)
    if str(data.decode()).endswith(".txt"):  
        print("Server received:", data.decode())
        try:
            f = open(str(data.decode()), "rb")
            l = f.read(1024)
            while (l):
               conn.send(l)
               print("Sent:", l.decode())
               l = f.read(1024)
            f.close()
            print("Done sending file contents")
        except:
            conn.send(("Server could not find file: " + data.decode()).encode())
        conn.close()
    
    else:
        print("Server received", data.decode())
        directoryName = data.decode()
        path = os.getcwd()
        directoryPath = path + "\\" + directoryName
        print(directoryPath)
        try:
            directoryList = os.listdir(directoryPath)
            print(" ".join(directoryList))
            conn.send((" ".join(directoryList)).encode())
        except:
            conn.send(("Server could not find directory: " + directoryName).encode())
        conn.close()