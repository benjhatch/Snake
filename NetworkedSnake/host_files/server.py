import socket
import threading
from queue import Queue
import pickle

class Server:
    def __init__(self, jungle):
        self.run = True
        self.snakes = jungle.snakes
        self.numSnakes = len(self.snakes)
        self.jungle = jungle
        self.all_connections = []
        self.all_address = []
        self.s = socket.socket()
        self.host = socket.gethostbyname(socket.gethostname())
        print("server will start on host", self.host)

        self.port = 8080
        self.s.bind((self.host,self.port))
        print("Server done binding to host and port successfully\n")

        self.q = Queue()
        print("Server is waiting for incoming connections")
        self.s.listen(5)
        self.acceptSocket()
        self.print_lock = threading.Lock()
        self.startThreads()

    def recvMessage(self,conn):
        while self.run:
            incoming_msg = conn.recv(1024)
            snakeInfo = pickle.loads(incoming_msg)
            self.snakes[snakeInfo[0]].changeDir(snakeInfo[1])

    def sendScreen(self):
        snakeLocations = []
        for snake in self.jungle.snakes:
            snakeInfo = [snake.color, list(snake.ownLocations.keys())]
            snakeLocations.append(snakeInfo)
        locations = [self.jungle.blockSize, snakeLocations, list(self.jungle.apples.keys())]
        message = pickle.dumps(locations)
        for conn in self.all_connections:
            conn.send(message)

    #SERVER START
    def resetConnections(self):
        for conn in self.all_connections:
            conn.close()
        del self.all_connections[:]
        del self.all_address[:]

    def acceptSocket(self):
        self.resetConnections()
        while len(self.all_connections) < self.numSnakes:
            conn, addr = self.s.accept()
            self.s.setblocking(1)
            self.all_connections.append(conn)
            self.all_address.append(addr)
            self.q.put(conn)
            print(addr, "Has connected to the server and is now online...\n")

    #THREADING FUNCTIONS
    def startThreads(self):
        for i in range(self.numSnakes):
            t = threading.Thread(target=self.threader)
            t.daemon = True
            t.start()

    def threader(self):
        while self.run:
            conn = self.q.get()
            self.recvMessage(conn)