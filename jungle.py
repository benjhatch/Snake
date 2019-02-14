from snake import Snake
from segment import Segment
import pygame as pg
import random
class Jungle:
    def __init__(self,rows,cols,blockSize,snakeCount,snakeLength):
        self.rows = rows
        self.cols = cols
        self.blockSize = blockSize
        self.colorList = [(0,255,0),(0,0,255)]
        self.screen = pg.display.set_mode((self.cols * self.blockSize, self.rows * self.blockSize))
        self.allSnakeLocations = set()
        self.snakes = self.initSnakes(snakeCount, snakeLength)
        self.keys = {pg.K_w: (0, 0), pg.K_d: (0, 1), pg.K_s: (0, 2), pg.K_a: (0, 3), pg.K_UP: (1, 0),
                     pg.K_RIGHT: (1, 1), pg.K_DOWN: (1, 2), pg.K_LEFT: (1, 3)}

    #JUNGLE IN ACTION
    def moveSnakes(self):
        size = len(self.snakes)
        i = 0
        snakeTotal = 0
        while i < size:
            snakeTotal += self.snakes[i].moveAlong()
            i+=1
        #if len(all snake locations) < snakeTotal
        #traverse snakes
            #if snakeHead is in snake before
                #that snake is out

    #INITIALIZING JUNGLE
    #snake making
    def initSnakes(self, count, length):
        snakes = []
        for i in range(count):
            row = random.randint(length, self.rows - 1)
            col = self.placeFirstPeice(length)
            dir = self.initDir(col)
            snakes.append(Snake(self.screen, self.blockSize, self.allSnakeLocations, [Segment((row, col), dir)], self.rows, self.cols, self.colorList[i]))
            self.allSnakeLocations.add((row,col))
            for j in range(length - 1):  # adding on rest of segments
                nextLocation = snakes[i].body[j].priorLoc()
                snakes[i].body.append(Segment(nextLocation, dir))
                self.allSnakeLocations.add(nextLocation)
        return snakes

    def placeFirstPeice(self, length):
        if length > self.cols / 2:
            return 0 + length
        else:
            out = random.randint(length-1, self.cols - length)
            return out

    def initDir(self, col):
        middle = self.cols // 2
        if col < middle:
            return 1  # right
        else:
            return 3  # left