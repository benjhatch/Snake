from jungle import Jungle
from server import Server
import pygame as pg
import time

run = True
timeLimit = 120
keyHit = False

def getJungle():
    default = input("Default Settings? 'y' for yes or 'n' for no: ")
    if default == 'y':
        jungle = Jungle(40, 40, 10, 1, 5, 1, 5)
    else:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        size = int(input("Enter segment size: "))
        numSnakes = int(input("Enter number of snakes: "))
        length = int(input("Enter snake length: "))
        numApples = int(input("Enter number of apples: "))
        increase = int(input("Enter snake gain upon apple contact: "))
        jungle = Jungle(rows, cols, size, numSnakes, length, numApples, increase)
    return jungle

#change me...use wasd for first snake
#rows, cols, size, number of snakes, length of snakes, number of apples, number added on contact with apple
jungle = getJungle()
server = Server(jungle)
pg.init()

while run:
    jungle.screen.fill((0, 0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    jungle.moveSnakes()
    server.sendScreen()
    pg.display.update()
    time.sleep(timeLimit / 5000)
