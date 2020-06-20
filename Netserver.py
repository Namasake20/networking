"""
set up a server that will receive a connection from a client,send a string to the client and close the connection
"""
import socket

HOST = "127.0.0.1"
PORT = 5000
counter = 0
FORMAT = 'utf-8'
#step1:create a socket
mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#step 2:bind the socket
mysocket.bind((HOST,PORT))

while 1:
    #step3 :prepare for a connection
    print("waiting for connection")
    mysocket.listen(1)

    #step 4:wait for and accept a connection
    connection,address = mysocket.accept()
    counter += 1

    print("Connection",counter,"received from:",address[0])

    #step 5:process connection
    connection.send(b"SERVER>>> connection successful")

    clientMessage = connection.recv(1024).decode(FORMAT)

    while clientMessage != "CLIENT>>> TERMINATE":
        
        if not clientMessage:
            break

        print(clientMessage)
        serverMessage = input("SERVER>>>")
        connection.send("SERVER>>>" + serverMessage)
        clientMessage = connection.recv(1024).decode(FORMAT)
    #step 6:close connection
    print("connection terminated")
    connection.close()



