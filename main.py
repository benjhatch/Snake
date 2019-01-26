from board import Board
import pygame as pg

timer = pg.time.Clock()
run = True
frameTimer = 0
timeLimit = 200
keyHit = False

grid = Board(15,15,2)
grid.makeSnakes(1,3)
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
                if event.key == pg.K_w:
                    grid.snakeList[0].changeDir(0)
                    grid.moveSnakes()
                elif event.key == pg.K_d:
                    grid.snakeList[0].changeDir(1)
                    grid.moveSnakes()
                elif event.key == pg.K_s:
                    grid.snakeList[0].changeDir(2)
                    grid.moveSnakes()
                elif event.key == pg.K_a:
                    grid.snakeList[0].changeDir(3)
                    grid.moveSnakes()
            if event.type == pg.QUIT:
                run = False
        if not keyHit:
            grid.moveSnakes()
        keyHit = False
        grid.displayGrid(screen)