import socket
class Server:
    def __init__(self,numSnakes = 1):
        self.numSnakes = numSnakes
        self.s = socket.socket()
        self.host = socket.gethostname()
        print("server will start on host", self.host)
        self.port = 8080
        self.s.bind((self.host,self.port))
        print("server is waiting for incoming connections")
        self.s.listen(numSnakes)
        self.conn, self.addr = self.s.accept()
        print(self.addr, "has connected to the server and is online")
        print()

    def pingClients(self):
        ping = "Send me the direction"
        ping = ping.encode()
        self.conn.send(ping)
        #now get the client direction
        for i in range(self.numSnakes):
            incoming = self.conn.recv(1024)
            incoming = incoming.decode()
            self.processMessage(incoming)

    def processMessage(self,incoming):
        print("Client: ", incoming)