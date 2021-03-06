import socket
import threading
import pickle
import pygame as pg


class Client:
    def __init__(self, ip, snakeColor):
        self.run = True

        self.s = socket.socket()
        self.host = ip #ENTER IP ADDRESS FOR HOST!!!
        self.port = 8080
        self.s.connect((self.host, self.port))
        self.index = self.recvDisplaySettings()
        print("Connected to snake server")
        self.keys = {pg.K_w: (self.index, 0), pg.K_d: (self.index, 1), pg.K_s: (self.index, 2), pg.K_a: (self.index, 3)}
        snakeColor = pickle.dumps(snakeColor)
        self.s.send(snakeColor)

        self.print_lock = threading.Lock()
        self.screen = pg.display.set_mode((self.cols * self.size, self.rows * self.size))
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
        apple_color = (255, 0, 0)
        snakeLocations = data[0]
        size = self.size
        apples = data[1]
        for snake in snakeLocations:
            snake_color = snake[0]
            locations = snake[1]
            for segment in locations:
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

    def recvDisplaySettings(self):
        settings = self.s.recv(1024)
        settings = pickle.loads(settings)
        self.rows = settings[0]
        self.cols = settings[1]
        self.size = settings[2]
        return settings[3] #snake index

ip = input("Server IP: ")
snakeColor = input("Enter the snake color like so ~ R,G,B: ")
client = Client(ip, snakeColor)