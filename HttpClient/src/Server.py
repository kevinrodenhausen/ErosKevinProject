'''
Created on Apr 17, 2019

@author: Kevin
'''
# -*- coding: utf-8 -*-
from test.test_decimal import file
from test.test_threadedtempfile import FILES_PER_THREAD
"""
Created on Tue Apr 16 21:12:30 2019
@author: erosg
"""

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_name = 'localhost'
server_address = (server_name, 60040)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(1)
connection, client_address = sock.accept()

filePath = 'C:\\Users\\Kevin\\Documents\\Communication Networks\\Random Files\\file1'
directoryName = 'Random Files'
fileName = 'file1'
feedback = -1
stringFeed = str(feedback)

message = connection.recv(1024).decode()
print(message)

while(message != directoryName):
    connection.send(stringFeed.encode())
    message = connection.recv(1024).decode()
    
#Once a good message received then we can send good feedback
feedback = 1
stringFeed = str(feedback)
connection.send(stringFeed.encode())
print('After feedBack sent')

#Now to send the number of files which will be 1 for this test.
counter = 1
connection.send((str(counter).encode()))
print('After counter sent')

while(counter <= 1):
    connection.send(fileName.encode())
    file = open(filePath)
    
    for line in file:
        connection.send(line.encode())
    
    connection.send('KevinEros'.encode())
    counter += 1
        
        
    
    
