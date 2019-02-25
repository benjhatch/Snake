import socket
import pickle
class Server:
    def __init__(self, snakes, numSnakes = 1):
        self.snakes = snakes
        self.screen = "screen"
        self.numSnakes = numSnakes
        self.s = socket.socket()
        self.host = socket.gethostname()
        print("server will start on host", self.host)
        self.port = 8080
        self.s.bind((self.host,self.port))
        print(self.numSnakes)
        print("server is waiting for incoming connections")
        for i in range(numSnakes):
            self.s.listen(numSnakes)
            self.conn, self.addr = self.s.accept()
        print(self.addr, "has connected to the server and is online")
        print()

    def pingClients(self):
        #now get the client direction
        for i in range(self.numSnakes):
            incoming = self.conn.recv(1024)
            incoming = pickle.loads(incoming)
            self.processMessage(incoming)
            self.sendScreen()

    def processMessage(self,incoming):
        snake = self.snakes[incoming[0]]
        snake.changeDir(incoming[1])
        #print("Client: ", incoming)

    def sendScreen(self):
        data = pickle.dumps(self.screen)
        self.conn.send(data)