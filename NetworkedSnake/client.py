import socket
import threading
import pickle
import pygame as pg


class Client:
    def __init__(self, number=0, cols=40, rows=40, blockSize=10):
        self.run = True
        self.keys = {pg.K_w: (number, 0), pg.K_d: (number, 1), pg.K_s: (number, 2), pg.K_a: (number, 3)}
        self.screen = pg.display.set_mode((cols * blockSize, rows * blockSize))

        self.s = socket.socket()
        self.host = socket.gethostbyname("Benjamins-MBP") #ENTER IP ADDRESS FOR HOST!!!
        self.port = 8080
        self.s.connect((self.host, self.port))
        print("Connected to chat server")

        self.print_lock = threading.Lock()
        pg.init()
        self.startThreads()
        self.sendDir()

    def startThreads(self):
        self.t1 = threading.Thread(target=self.recvScreen)
        self.t1.start()

    def recvScreen(self):
        while self.run:
            incoming_message = self.s.recv(1024)
            incoming_message = pickle.loads(incoming_message)
            self.drawScreen(incoming_message)

    def drawScreen(self, data):
        self.screen.fill((0,0,0))
        snake_color = (0, 255, 0)
        apple_color = (255, 0, 0)
        size = data[0]
        snakeLocations = data[1]
        apples = data[2]
        for segment in snakeLocations:
            pg.draw.rect(self.screen, snake_color, ((segment[1] * size), (segment[0] * size), size - 2, size - 2))
        for location in apples:
            pg.draw.rect(self.screen, apple_color, ((location[1] * size), (location[0] * size), size - 2, size - 2))
        pg.display.update()

    def sendDir(self):
        while self.run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
                if event.type == pg.KEYDOWN and event.key in self.keys:
                    snakeInfo = pickle.dumps(self.keys[event.key])
                    self.s.send(snakeInfo)

#snakeNum = int(input("Enter the number of the snake: "))
client = Client()  # put the snake you want to control in the parentheses...