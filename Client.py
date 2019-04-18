# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 21:44:35 2019

@author: erosg
"""

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port on the server given by the caller
server_address = (sys.argv[1], 10000)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
#    '''
    message = 'This is the message.  It will be repeated.'
    print('sending "%s"' % message)
    sock.sendall(message.encode())

    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received "%s"' % data.decode())
#    '''
#    message = input("What is the name of the target directory?:")
#    sock.sendall(message.encode())
    
finally:
    sock.close()