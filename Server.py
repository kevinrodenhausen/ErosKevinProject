# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 21:12:30 2019

@author: erosg
"""

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_name = sys.argv[1]
server_address = (server_name, 10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(1)
#'''
while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('client connected:', client_address)
        while True:
            data = connection.recv(16)
            print('received "%s"' % data.decode())
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()
#'''
#while