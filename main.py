from board import Board
import pygame as pg

timer = pg.time.Clock()
run = True
frameTimer = 0
timeLimit = 130
keyHit = False

#change me...use wasd for first snake
board = Board(15,15,50,1,4,1) #rows, cols, size, number of snakes, length of snakes, number of apples
snakes = board.snakes
#cool :)

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