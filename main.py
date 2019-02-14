from jungle import Jungle
import pygame as pg

timer = pg.time.Clock()
run = True
frameTimer = 0
timeLimit = 120
keyHit = False

#change me...use wasd for first snake
jungle = Jungle(20,20,10,1,5) #rows, cols, size, number of snakes, length of snakes, ?number of apples?
pg.init()

while run:
    timer.tick()
    frameTimer += timer.get_rawtime()
    if frameTimer > timeLimit:
        frameTimer = 0
        jungle.screen.fill((0, 0, 0))
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key in jungle.keys:
                keyHit = True
                tuple = jungle.keys[event.key]
                snake = jungle.snakes[tuple[0]]
                snake.changeDir(tuple[1])
                jungle.moveSnakes()
            if event.type == pg.QUIT:
                run = False
        if not keyHit:
            jungle.moveSnakes()
        keyHit = False
        pg.display.update()