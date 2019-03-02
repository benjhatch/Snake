import socket
import threading
import pickle
import pygame as pg

class Client:
    def __init__(self, number = 0):
        self.run  = True
        self.keys = {pg.K_w: (number, 0), pg.K_d: (number, 1), pg.K_s: (number, 2), pg.K_a: (number, 3)}

        self.s = socket.socket()
        self.host = input("Please enter the hostname of the server: ")
        self.port = 8080
        self.s.connect((self.host,self.port))
        print("Connected to chat server")

        self.print_lock = threading.Lock()
        pg.init()
        self.startThreads()
        self.sendDir()

    def startThreads(self):
        self.t1 = threading.Thread(target = self.recvMsg)
        self.t1.start()

    def recvMsg(self):
        while self.run:
            incoming_message = self.s.recv(1024)
            incoming_message = incoming_message.decode()
            if len(incoming_message) > 0:
                with self.print_lock:
                    print("Server: ", incoming_message)

    def sendDir(self):
        while self.run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
                if event.type == pg.KEYDOWN and event.key in self.keys:
                    snakeInfo = pickle.dumps(self.keys[event.key])
                    self.s.send(snakeInfo)

client = Client() #put the snake you want to control in the parentheses...