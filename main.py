from board import Board
import pygame as pg

timer = pg.time.Clock()
run = True
frameTimer = 0
timeLimit = 120
keyHit = False

#change me...use wasd for first snake
board = Board(30,30,10,1,4,1) #rows, cols, size, number of snakes, length of snakes, number of apples
#cool :)

snakes = board.snakes
screen = pg.display.set_mode((board.cols * board.size, board.rows * board.size))
pg.init()


while run:
    timer.tick()
    frameTimer += timer.get_rawtime()
    if frameTimer > timeLimit:
        frameTimer = 0
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                keyHit = True
                snake = board.determineSnake(event.key) #update this
                keys = board.determineKeys(snake) #update this
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