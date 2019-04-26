# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 01:02:48 2019

@author: erosg
"""
import socket
from socket import *
import sys

if len(sys.argv) != 2:
    print("Required Format: python FTTCPClient.py <server ip>")
    sys.exit()

clientSocket = socket(AF_INET, SOCK_STREAM) # Create TCP socket object
host = sys.argv[1] # IP Address of TCPServer
port = 50000

clientSocket.connect((host, port))
if input("Would you like to request a specific file or directory? (F / D): ") == "F":
    success = False
    targetFile = input("What is the name of the file? (include '.txt'): ")
    clientSocket.send((targetFile).encode())
    with open(targetFile, "wb") as f:
        print("New file created")
        while True:
            # print("data is coming in...")
            data = clientSocket.recv(1024)
            print(data.decode())
            if str(data.decode()).startswith("Server could not"):
                f.close()
                print("File not found on server, this file transfer aborted. New file "
                      + "created in directory is empty.")
                clientSocket.close()
                print("Connection has been closed")
                break
            # print("data = %s", (data))
            if not data:
                break
            f.write(data)
            success = True
    f.close()
    if success == True:
        print(targetFile, "successfully transfered")
        clientSocket.close()
        print("Connection has been closed")
else:
    targetDirectory = input("What is the name of the directory?: ")
    clientSocket.send((targetDirectory).encode())
    filesList = clientSocket.recv(1024)
    if str(filesList.decode()).startswith("Server could not"):
        print(str(filesList.decode()))
        clientSocket.close()
        print("Connection has been closed")
    else:
        print(str(filesList.decode()).split())
        clientSocket.close()
        for file in filesList.decode().split():
            clientSocket = socket(AF_INET, SOCK_STREAM) # Create TCP socket object        
            host = sys.argv[1] # IP Address of TCPServer
            port = 50000
            clientSocket.connect((host, port))
            clientSocket.send((targetDirectory + "\\" + file).encode())
            
            with open(file, "wb") as f:
                print("New file created")
                while True:
                    # print("data is coming in...")
                    data = clientSocket.recv(1024)
                    # print("data = %s", (data))
                    if not data:
                        break
                    f.write(data)
            f.close()
            print(file, "successfully transfered")
            clientSocket.close()
            print("Connection has been closed")
