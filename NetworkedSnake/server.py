import socket
import threading
from queue import Queue
import pickle
import time

class Server:
    def __init__(self, snakes, numSnakes = 1):
        self.run = True
        self.snakes = snakes
        self.numSnakes = numSnakes
        self.all_connections = []
        self.all_address = []
        self.s = socket.socket()
        self.host = socket.gethostname()
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

    def sendMessage(self):
        while self.run:
            message = "this is the screen"
            for conn in self.all_connections:
                conn.send(message.encode())
            time.sleep(3)

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
        sendingThread = threading.Thread(target=self.sendMessage)
        sendingThread.start()
        for i in range(self.numSnakes):
            t = threading.Thread(target=self.threader)
            t.daemon = True
            t.start()

    def threader(self):
        while self.run:
            conn = self.q.get()
            self.recvMessage(conn)