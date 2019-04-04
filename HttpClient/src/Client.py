'''

@author: Kevin
'''

import sys
import os
from socket import *

def main():
    clientSocket = setConnection()
    userInput = input('Type 1 if you want to request a directory.')
        
    while(userInput == 1):
        fileAmount = requestDirectory(clientSocket)
        downloadContent(clientSocket, fileAmount)
        userInput = input('Type 1 if you want to request a directory.')
        
    clientSocket.close()
    
    
#Set up the connection to start communication between client and server
def setConnection():
    serverName = 'localHost' #This will have to be changed to the actual server name
    serverPort = 60040
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    return clientSocket
    
#Obtains user input for a directory name
def requestDirectory(clientSocket):
    #feedBack returns how many files are in the directory or -1 if there is no directory by that name.
    feedBack = -1 
    
    while(feedBack == -1):
        directoryName = input('Please specify a valid directory name\n')
        clientSocket.send(directoryName.encode())
        feedBack = clientSocket.recv(1024).decode()
    
    return feedBack

#Copies the content of all the files into various files.
def downloadContent(clientSocket, fileAmount):
    #First make a directory to hold all the files
    #This won't work if intermediate directories don't exist...
    #This path is specific for my computer, and this may not be implemented this way.
    #A function called make mkdirs can be used to make a path
    #Users may not want this program creating random directories on their machine...
    path = 'C:\\Users\\Kevin\\Documents\\Communication Networks\\Random Files'
    counter = 1
    fileNumber = str(counter)
    fileName = '\\file'
    fileEnd = -1
    condition = True
    
    #Hopefully this will be in sync with the server when reading files
    while(counter < fileAmount):
        fullFilename = fileName + fileNumber
        fullPath = path + fullFilename
        file = open(fullPath,"a")
        
        #Infinite loop here
        #How do we check that server is done with one file and is about to read the contents of the next?
        while(condition):
            line = clientSocket.recv(1024).decode()
        
        file.write(line)
        counter += 1
        fileNumber = str(counter)
        
        
    
    

if __name__ == '__main__':
    main()