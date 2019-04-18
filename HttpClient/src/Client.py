'''

@author: Kevin
'''

import sys
import os
from socket import *

def main():
    clientSocket = setConnection()
    requestDirectory(clientSocket)
    userInput = input('Type 1 if you want to request a directory.')
    int(userInput)
    print(userInput)
        
    while(userInput == 1):
        requestDirectory(clientSocket)
        userInput = -1
        userInput = input('Type 1 if you want to request a directory.')
        
    clientSocket.close()
    
    
#Set up the connection to start communication between client and server
def setConnection():
    serverName = 'localhost' #This is specific for my machine you will have to change it!
    serverPort = 60040
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    return clientSocket
    
#Obtains user input for a directory name
def requestDirectory(clientSocket):
    #feedBack returns how many files are in the directory or -1 if there is no directory by that name.
    feedBack = -1 
    print('In requestDirectory')
    while(feedBack == -1):
        directoryName = input('Please specify a valid directory name\n')
        clientSocket.send(directoryName.encode())
        feedBack = int(clientSocket.recv(1024).decode())
        print('feedBack is: ', feedBack)
        
    downloadContent(clientSocket,feedBack,directoryName)

#Copies the content of all the files into various files.
def downloadContent(clientSocket, fileAmount, directoryName):
    #First make a directory to hold all the files
    #This won't work if intermediate directories don't exist...
    #This path is specific for my computer, and this may not be implemented this way.
    #A function called make mkdirs can be used to make a path
    #Users may not want this program creating random directories on their machine...
    #I'm using Temp but when it's actually implemented it will be directoryName
    path = 'C:\\Users\\Kevin\\Documents\\Communication Networks\\' + 'Temp\\'
    stringCounter = clientSocket.recv(1024).decode()
    print('Counter is: ' + stringCounter)
    counter = int(stringCounter)
    #fileNumber = str(counter)
    EOF = 'KevinEros'
    
    #Hopefully this will be in sync with the server when reading files
    while(counter <= fileAmount):
        fileName = clientSocket.recv(1024).decode()
        print(fileName)
        fullPath = path + fileName
        print(fullPath)
        file = open(fullPath,"a")
        
        #Reading a line from the server and writing to the file.
        while True:
            line = clientSocket.recv(1024).decode()
            print(line)
            if(EOF == line):
                break
            
            file.write(line)
        
        counter += 1
        
        
    
    

if __name__ == '__main__':
    main()