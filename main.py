from board import Board
import pygame as pg

timer = pg.time.Clock()
run = True
frameTimer = 0
timeLimit = 120
keyHit = False

#change me...use wasd for first snake
board = Board(40,40,20,2,6,6) #rows, cols, size, number of snakes, length of snakes, number of apples
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
            if event.type == pg.KEYDOWN and event.key in board.keys:
                keyHit = True
                tuple = board.keys[event.key]
                snake = snakes.nest[tuple[0]]
                snake.changeDir(tuple[1])
                snakes.advance()
            if event.type == pg.QUIT:
                run = False
        if not keyHit:
            snakes.advance()
        keyHit = False
        board.displayGame(screen)