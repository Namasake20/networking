"""
set up a client that will read information sent from a server and display that unformation.
"""
import socket

HOST = "127.0.0.1"
PORT = 5000
FORMAT = 'utf-8'
#step 1:create a socket
print("Attempting a connection")
mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#step 2:connect to server
mysocket.connect((HOST,PORT))
print("Connected to Server")

#step 3:process connection
serverMessage = mysocket.recv(1024).decode(FORMAT)

while serverMessage != "SERVER>>> TERMINATE":

    if not serverMessage:
        break
    
    print(serverMessage)
    clientMessage = input("CLIENT>>>")
    mysocket.send(b"CLIENT>>>" + clientMessage)
    serverMessage = mysocket.recv(1024).decode(FORMAT)

#step 4:close connection
print("connection terminated")
mysocket.close()


