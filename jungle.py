from snake import Snake
from segment import Segment
from apple_tree import AppleTree
import pygame as pg
import random
class Jungle:
    def __init__(self,rows,cols,blockSize,snakeCount,snakeLength, numApples):
        self.rows = rows
        self.cols = cols
        self.blockSize = blockSize
        self.colorList = [(0,255,0),(0,0,255),(255,255,255),(100,100,150)]
        self.screen = pg.display.set_mode(((self.cols) * self.blockSize, (self.rows) * self.blockSize))
        self.allSnakeLocations = set() #keeps track of all snake locations in one list
        self.tailLocations = set()
        self.apples = AppleTree(self.screen, blockSize, rows, cols, self.allSnakeLocations, numApples)
        self.snakes = self.initSnakes(snakeCount, snakeLength)
        self.keys = {pg.K_w: (0, 0), pg.K_d: (0, 1), pg.K_s: (0, 2), pg.K_a: (0, 3), pg.K_UP: (1, 0),
                     pg.K_RIGHT: (1, 1), pg.K_DOWN: (1, 2), pg.K_LEFT: (1, 3)}

    #JUNGLE IN ACTION
    def moveSnakes(self):
        self.allSnakeLocations.clear()
        self.tailLocations.clear()
        self.snakeHeads = []
        i = 0
        lengthOfAllSnakes = 0
        self.apples.drawApples()
        while i < len(self.snakes):
            lengthOfAllSnakes += self.snakes[i].moveAlong()
            i+=1
        if len(self.allSnakeLocations) < lengthOfAllSnakes:
            toBeCleared = []
            snakeHeads = [snake.body[0].loc for snake in self.snakes if not snake.out]
            for i in range(len(self.snakes)):
                loc = self.snakes[i].body[0].loc
                if not self.snakes[i].out and (loc in self.tailLocations or snakeHeads.count(loc) > 1):
                    toBeCleared.append(i)
            for i in range(len(toBeCleared)):
                self.snakes[toBeCleared[i]].clear()

    #INITIALIZING JUNGLE
    #snake making
    def initSnakes(self, count, length):
        snakes = []
        for i in range(count):
            row = random.randint(length, self.rows - 1)
            col = self.placeFirstPeice(length)
            dir = self.initDir(col)
            snakes.append(Snake(self.screen, self.blockSize, self.apples, self.allSnakeLocations, self.tailLocations, [Segment((row, col), dir)], self.rows, self.cols, self.colorList[i]))
            for j in range(length - 1):  # adding on rest of segments
                nextLocation = snakes[i].body[j].priorLoc(dir)
                snakes[i].body.append(Segment(nextLocation, dir))
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