from snake import Snake
from segment import Segment
#from apple_tree import AppleTree
import pygame as pg
import random
class SnakeNest:
    def __init__(self, size, rows=0, cols=0, numSnakes=0, length=0):
        self.rows = rows
        self.cols = cols
        self.nest = self.makeSnakes(numSnakes, length)
        self.size = size
        self.keys = {pg.K_w: (0, 0), pg.K_d: (0, 1), pg.K_s: (0, 2), pg.K_a: (0, 3), pg.K_UP: (1, 0),
                     pg.K_RIGHT: (1, 1), pg.K_DOWN: (1, 2), pg.K_LEFT: (1, 3)}
        self.screen = pg.display.set_mode((self.cols * self.size, self.rows * self.size))

    def makeSnakes(self,numSnakes, length): #need to update placement
        list = []
        for i in range(numSnakes):
            row = random.randint(0, self.rows-1)
            col = random.randint(length, self.cols - length)
            possibleLoc = (row,col)
            dir = self.setDir(possibleLoc[1])  # gives the column the snake head is in, may consider revising
            list.append(Snake([Segment(possibleLoc, dir)]))
            for j in range(length-1):
                nextLoc = list[i].body[j].priorLoc()
                list[i].body.append(Segment(nextLoc,dir))
        return list

    def setDir(self,col):
        middle = self.cols // 2
        if col < middle:
            return 1 #right
        else:
            return 3 #left

    def advance(self,i = 0):
        snake = self.nest[i]
        if i == len(self.nest) -1:
            snake.moveAlong(self.screen, self.size)
        else:
            snake.moveAlong(self.snakeHitApple(i))
            self.advance(i + 1)

    def clear(self, snake):
        snake.out = True
        snake.body = []
        snake.locations = {}

    def snakeHitApple(self, i): #may need to update placement of apple upon hit and error thrown
        if self.nest[i].out:
            return False
        apples = self.apples
        head = (self.nest[i].body[0].loc[0],self.nest[i].body[0].loc[1])
        if head in apples.tree:
            loc = apples.tree[head].changeLoc(self.rows,self.columns,apples.tree)
            apples.tree[loc] = apples.tree.pop(head)
            return True
        return False