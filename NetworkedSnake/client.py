import socket
import threading
import pickle
import pygame as pg
import time


class Client:
    def __init__(self, number=0, cols=40, rows=40, blockSize=10):
        self.run = True
        self.keys = {pg.K_w: (number, 0), pg.K_d: (number, 1), pg.K_s: (number, 2), pg.K_a: (number, 3)}
        self.screen = pg.display.set_mode((cols * blockSize, rows * blockSize))

        self.s = socket.socket()
        self.host = "Benjamins-MBP"
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

    def drawScreen(self, locations):
        self.screen.fill((0,0,0))
        color = (0, 255, 0)
        size = 10
        for segment in locations:
            pg.draw.rect(self.screen, color, ((segment[1] * size), (segment[0] * size), size - 2, size - 2))
        pg.display.update()

    def sendDir(self):
        while self.run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
                if event.type == pg.KEYDOWN and event.key in self.keys:
                    snakeInfo = pickle.dumps(self.keys[event.key])
                    self.s.send(snakeInfo)


client = Client()  # put the snake you want to control in the parentheses...