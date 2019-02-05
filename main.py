from board import Board
import pygame as pg

timer = pg.time.Clock()
run = True
frameTimer = 0
timeLimit = 100
keyHit = False

#still need to fix minor bugs :(

#change me...use wasd for first snake
board = Board(15,15,1,4,1) #rows, cols, number of snakes, length of snakes, number of apples
snakes = board.snakes
#cool :)

screen = pg.display.set_mode((board.rows * 50, board.cols * 50))
pg.init()


while run:
    timer.tick()
    frameTimer += timer.get_rawtime()
    if frameTimer > timeLimit:
        frameTimer = 0
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                keyHit = True
                snake = board.determineSnake(event.key)
                keys = board.determineKeys(snake)
                if event.key == keys[0]:
                    snake.changeDir(0)
                    snakes.moveSnakes()
                elif event.key == keys[1]:
                    snake.changeDir(1)
                    snakes.moveSnakes()
                elif event.key == keys[2]:
                    snake.changeDir(2)
                    snakes.moveSnakes()
                elif event.key == keys[3]:
                    snake.changeDir(3)
                    snakes.moveSnakes()
            if event.type == pg.QUIT:
                run = False
        if not keyHit:
            snakes.moveSnakes()
        keyHit = False
        board.displayGame(screen)