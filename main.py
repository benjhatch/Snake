from board import Board
import pygame as pg

timer = pg.time.Clock()
run = True
frameTimer = 0
timeLimit = 200
keyHit = False

grid = Board(15,15,1)
grid.makeSnakes(2,3)
screen = pg.display.set_mode((grid.rows * 50, grid.cols * 50))
pg.init()


while run:
    timer.tick()
    frameTimer += timer.get_rawtime()
    if frameTimer > timeLimit:
        frameTimer = 0
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                keyHit = True
                snake = grid.determineSnake(event.key)
                keys = grid.determineKeys(snake)
                if event.key == keys[0]:
                    snake.changeDir(0)
                    grid.moveSnakes()
                elif event.key == keys[1]:
                    snake.changeDir(1)
                    grid.moveSnakes()
                elif event.key == keys[2]:
                    snake.changeDir(2)
                    grid.moveSnakes()
                elif event.key == keys[3]:
                    snake.changeDir(3)
                    grid.moveSnakes()
            if event.type == pg.QUIT:
                run = False
        if not keyHit:
            grid.moveSnakes()
        keyHit = False
        grid.displayGrid(screen)