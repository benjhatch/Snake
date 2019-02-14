from snake import Snake
from segment import Segment
import pygame as pg
import random
class Jungle:
    def __init__(self,rows,cols,blockSize,snakeCount,snakeLength):
        self.rows = rows
        self.cols = cols
        self.blockSize = blockSize
        self.screen = pg.display.set_mode((self.cols * self.blockSize, self.rows * self.blockSize))
        self.snakes = self.initSnakes(snakeCount, snakeLength)
        self.keys = {pg.K_w: (0, 0), pg.K_d: (0, 1), pg.K_s: (0, 2), pg.K_a: (0, 3), pg.K_UP: (1, 0),
                     pg.K_RIGHT: (1, 1), pg.K_DOWN: (1, 2), pg.K_LEFT: (1, 3)}

    #while jungle is in action
    def moveSnakes(self):
        if len(self.snakes) > 0:
            i = 0
            while i < len(self.snakes):
                self.snakes[i].moveAlong()
                i+=1

    # initializing the jungle
    def initSnakes(self, count, length):
        snakes = []
        for i in range(count):
            row = random.randint(length, self.rows - 1)
            col = self.placeFirstPeice(length)
            dir = self.initDir(col)
            snakes.append(Snake(self.screen, self.blockSize, [Segment((row, col), dir)], self.rows, self.cols))
            for j in range(length - 1):  # adding on rest of segments
                nextLocation = snakes[i].body[j].priorLoc()
                snakes[i].body.append(Segment(nextLocation, dir))
        return snakes

    def placeFirstPeice(self, length):
        if length > self.cols / 2:
            return 0 + length
        else:
            return random.randint(length, self.cols - (length + 1))

    def initDir(self, col):
        middle = self.cols // 2
        if col < middle:
            return 1  # right
        else:
            return 3  # left