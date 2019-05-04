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

        self.port = 8080
        try:
            self.s.bind((self.host,self.port))
        except:
            print("unable to bind host and port...check if port is active")
        print("Server done binding to host and port successfully\n")

        self.q = Queue()
        print("Server is waiting for incoming connections")
        print("server will start on host", self.host)
        print("Copy ip and paste into client input upon client startup")
        self.s.listen(len(jungle.snakes))
        self.acceptSocket()
        self.print_lock = threading.Lock()
        self.startThreads()

    def recvMessage(self,conn):
        individualConn = True
        while self.run and individualConn:
            try:
                incoming_msg = conn.recv(1024)
                snakeInfo = pickle.loads(incoming_msg)
                self.snakes[snakeInfo[0]].changeDir(snakeInfo[1])
            except:
                individualConn = False
                print(conn, "has quit")

    def sendScreen(self):
        snakeLocations = []
        for snake in self.jungle.snakes:
            snakeInfo = [snake.color, list(snake.ownLocations.keys())]
            snakeLocations.append(snakeInfo)
        locations = [snakeLocations, list(self.jungle.apples.keys())]
        message = pickle.dumps(locations)
        for conn in self.all_connections:
            try:
                conn.send(message)
            except:
                conn.close()
                print("no longer sending screen to", conn)
                self.all_connections.remove(conn)

    #SERVER START
    def resetConnections(self):
        for conn in self.all_connections:
            conn.close()
        del self.all_connections[:]
        del self.all_address[:]

    def acceptSocket(self):
        self.resetConnections()
        snakeIndex = 0
        while len(self.all_connections) < self.numSnakes:
            conn, addr = self.s.accept()
            self.s.setblocking(1)
            self.all_connections.append(conn)
            self.all_address.append(addr)
            self.sendDisplaySettings(conn, snakeIndex)
            self.q.put(conn)
            print(addr, "Has connected to the server and is now online...\n")
            snakeIndex += 1

    def sendDisplaySettings(self, conn, snakeIndex):
        settings = [self.jungle.rows, self.jungle.cols, self.jungle.blockSize, snakeIndex]
        msg = pickle.dumps(settings)
        conn.send(msg)
        self.recvColor(conn, snakeIndex)

    def recvColor(self, conn, snakeIndex):
        incoming_msg = conn.recv(1024)
        snakeColor = pickle.loads(incoming_msg)
        snakeColor = snakeColor.split(",")
        for i in range(len(snakeColor)):
            snakeColor[i] = int(snakeColor[i])
        snakeColor = (snakeColor[0], snakeColor[1], snakeColor[2])
        self.jungle.snakes[snakeIndex].color = snakeColor

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