# -*- coding: utf-8 -*-
import socket
from _thread import * #supposed to be _thread but python 2.7 uses thread so to run in terminal remove underscore

position = ["0:(435,75)", "1:(450,50)"]
clientID = "0" #0 represents first clinet

def clientThread(conn):
    global clientID
    global position
    conn.send(str.encode(clientID)) #sends default utf-8 encoded version of string
    clientID = "1" #id 1 represents second client
    running = True
    while running:
        try:
            data = conn.recv(1024) #The return value is a string representing the data received. The maximum amount of data to be received at once is specified by bufsize which is 1024 in this case
            message = data.decode('utf-8') #decodes utf-8 encoded string received in data
            if not data:
                conn.send(str.encode("Closing"))
                break
            else:
                print("Recieved: " + message)
                arr = message.split(":")
                client = int(arr[0])
                position[client] = message

                if client == 0:
                    other = 1
                    other2 = 2
                elif client == 1:
                    other = 0
                    other2 = 2
                else:
                    other = 0
                    other2 = 1

                message = position[other][:]
                #reply2 = pos[other2][:]
                print("Sent: " + message)
                #print("Sent: " + reply2)

            conn.sendall(str.encode(message))
            #conn.sendall(str.encode(reply2))
        except:
            break
    conn.close()
    print("Connection ended")

####################################### WHERE RUNNING SERVER STARTS ##################################################
# creating socket connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#defining server and port
port = 2004 #Port to listen on and accept connections
serverName = 'cheshire.cse.buffalo.edu' #name of server, if empty string is passed the server accpets connections on all IPv4 interfaces
serverIP = socket.gethostbyname(serverName) #getting ip addresss of cheshire.cse.buffalo.edu

#binding server to my port
try:
    s.bind((serverName, port))
except socket.error as err:
    print(str(err))

# Listening for connections to the server. Rn set at a max of 2 connections
s.listen(2)
print("Server is ready and listening for connections")

#This loop is responsible for getting all the different connections and for each connection we start a new thread
#This loop will continue running while the function up above this running at the same time
while True:
    conn, addr = s.accept() # .accept() blocks and waits for an incoming connection.
                            # When client connects, it returns a new socket object representing the connection and a tuple holding the address of the client.
                            # Socket returned is the one that will be used to communicate with the client.
                            # It’s distinct from the listening socket that the server is using to accept new connections
    print("Connected to: ", addr)

    start_new_thread(clientThread, (conn,))
    #Start a new thread and return its identifier.
    # The thread executes the function clientThread with the argument list args which are a tuple