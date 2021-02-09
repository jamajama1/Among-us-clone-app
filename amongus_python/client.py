import socket

#Network class is made for setting up on the client side connecting to the server
class Client:
    #Creating new Client
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating new TCP socket
        self.port = 2004
        self.host = "128.205.32.39" #cheshire ip is 128.205.32.39 mine is 192.168.1.190
        self.addr = (self.host, self.port)
        self.id = self.link()

    def sendData(self, data): #data is a str containing data to be transmitted
        try:
            self.client.send(str.encode(data))
            message = self.client.recv(1024).decode()
            return message
        except socket.error as e:
            error = str(e)
            return error

    def link(self):
        self.client.connect(self.addr) #connecting client to server
        connection = self.client.recv(1024).decode()
        return connection
