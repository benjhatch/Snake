import socket
import pickle
import pygame as pg

class Client:
    def __init__(self,snakeIndex):
        self.dir = (snakeIndex, 1)
        self.s = socket.socket()
        self.host = input("Enter server hostname: ")
        self.port = 8080
        self.s.connect((self.host,self.port))
        print("Connected to server...Activating Client")
        self.keys = self.makeKeys(snakeIndex)
        pg.init()
        self.run = True
        self.activateClient()

    def activateClient(self):
        while self.run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
                if event.type == pg.KEYDOWN and event.key in self.keys:
                    self.dir = self.keys[event.key]
            message = pickle.dumps(self.dir)
            self.s.send(message)
            #now receive the screen
            incoming = self.s.recv(1024)
            #incoming = pickle.loads(incoming)
            #print(incoming)

    def makeKeys(self, index):
        return {pg.K_w: (index, 0), pg.K_d: (index, 1), pg.K_s: (index, 2), pg.K_a: (index, 3)}

client1 = Client(0)