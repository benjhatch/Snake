import socket
import pygame as pg

class Client:
    def __init__(self):
        self.dir = "1"
        self.s = socket.socket()
        self.host = input("Enter server hostname: ")
        self.port = 8080
        self.s.connect((self.host,self.port))
        print("Connected to server...Activating Client")
        self.keys = {pg.K_w: (0, 0), pg.K_d: (0, 1), pg.K_s: (0, 2), pg.K_a: (0, 3)}
        pg.init()
        self.run = True
        self.activateClient()

    def activateClient(self):
        while self.run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
                if event.type == pg.KEYDOWN and event.key in self.keys:
                    self.dir = str(self.keys[event.key])
            incoming = self.s.recv(1024)
            #after getting message
            print("got ping")
            print("sending direction")
            message = self.dir.encode()
            self.s.send(message)
            print("direction sent")
            print()
client = Client()