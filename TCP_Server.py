#!/usr/bin/python3

import socket

#Creating socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname() #Host is the server IP
port = 444  #Port to listen on

#Binding to socket
serversocket.bind((host, port))

#Starting TCP listener
serversocket.listen(3)

while True:
    #Starting the connection
    clientsocket, address = serversocket.accept()
    print("Recieved connection from %s ") % str(address)

    #Message after successful connection
    message = 'Server is connected' + "\r\n"
    clientsocket.send(message)

    clientsocket.close()
 