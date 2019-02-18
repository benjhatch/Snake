from jungle import Jungle
import pygame as pg
import time

timer = pg.time.Clock()
run = True
timeLimit = 5000
keyHit = False

#change me...use wasd for first snake
jungle = Jungle(50, 50, 10, 3, 10) #rows, cols, size, number of snakes, length of snakes, ?number of apples?
pg.init()

while run:
    jungle.screen.fill((0, 0, 0))
    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key in jungle.keys:
            tuple = jungle.keys[event.key]
            snake = jungle.snakes[tuple[0]]
            snake.changeDir(tuple[1])
        if event.type == pg.QUIT:
            run = False
    if not jungle.hit:
        jungle.moveSnakes()
    jungle.hit = False
    pg.display.update()
    time.sleep(timeLimit / 5000)