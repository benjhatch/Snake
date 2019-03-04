from jungle import Jungle
from server import Server
import pygame as pg
import time

run = True
timeLimit = 500
keyHit = False

#change me...use wasd for first snake
#rows, cols, size, number of snakes, length of snakes, number of apples, number added on contact with apple
jungle = Jungle(40, 40, 10, 1, 5, 3, 5)
server = Server(jungle)
pg.init()

while run:
    jungle.screen.fill((255, 255, 255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    jungle.moveSnakes()
    server.sendScreen()
    pg.display.update()
    time.sleep(timeLimit / 5000)
