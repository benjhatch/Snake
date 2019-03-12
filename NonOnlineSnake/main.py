from jungle import Jungle
import pygame as pg
import time

run = True
timeLimit = int(input("Enter snake speed (try 100): "))
keyHit = False

#change me...use wasd for first snake
#rows, cols, size, number of snakes, length of snakes, number of apples, number added on contact with apple
jungle = Jungle()
pg.init()

while run:
    jungle.screen.fill((0, 0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN and event.key in jungle.keys:
            tuple = jungle.keys[event.key]
            snake = jungle.snakes[tuple[0]]
            snake.changeDir(tuple[1])
    jungle.moveSnakes()
    pg.display.update()
    time.sleep(timeLimit / 5000)
