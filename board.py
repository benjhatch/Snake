from snake import Snake
from segment import Segment
from apple_tree import AppleTree
import random
import pygame as pg

class Board:
    def __init__(self,rows=0, cols=0, numSnakes=1, length=3, apples=1):
        self.rows = rows
        self.cols = cols
        self.grid = self.makeGrid()
        self.snakeList = self.makeSnakes(numSnakes,length)
        self.snakeLocations = [snake.locations for snake in self.snakeList if not snake.out]
        self.apples = AppleTree(apples,self.grid)

    def makeGrid(self):
        grid = []
        for r in range(self.rows):
            grid.append([])
            for c in range(self.cols):
                grid[r].append("+")
        return grid

    def getDir(self,col):
        middle = self.cols // 2
        if col < middle:
            return 1
        else:
            return 3

    def makeSnakes(self,numSnakes,length = 3):
        list = []
        for i in range(numSnakes):
            row = random.randint(length, self.rows - length)
            col = random.randint(length, self.cols - length)
            possibleLoc = [row,col]
            if possibleLoc in list:
                i -= 1
            else:
                dir = self.getDir(possibleLoc[1])
                list.append(Snake([Segment("o",possibleLoc,dir)]))
                for j in range(length-1):
                    possibleLoc = list[i].body[j].priorLoc()
                    list[i].body.append(Segment("o",possibleLoc,dir))
        return list

    def moveSnakes(self):
        for i in range(len(self.snakeList)):
            if not self.snakeList[i].out:
                snake = self.snakeList[i]
                snake.moveAlong(self.apples.snakeHitApple(snake))
                self.snakeLocations[i] = snake.locations
                self.checkOutOfBounds(self.snakeList[i])

    def checkOutOfBounds(self, snake):
        if len(snake.body) > 0:
            firstLoc = snake.body[0].loc
            if (firstLoc[1] > len(self.grid[0]) - 1 or firstLoc[1] < 0) or (firstLoc[0] > len(self.grid) - 1 or firstLoc[0] < 0):
                snake.out = True
                snake.body = []
            elif self.grid[firstLoc[0]][firstLoc[1]] not in ["A", "+"]:
                snake.out = True
                snake.body = []

    def displayGrid(self,screen):
        screen.fill((0,0,0))
        for apple in self.apples.appleTree:
            pg.draw.rect(screen, (255, 0, 0), ((apple.loc[1] * 50) + 1, (apple.loc[0] * 50) + 1, 48, 48))
        for i in range(len(self.snakeList)):
            for segment in self.snakeList[i].body:
                if i == 0:
                    color = (0, 255, 0)
                else:
                    color = (0, 0, 255)
                pg.draw.rect(screen, color, ((segment.loc[1] * 50) + 1, (segment.loc[0] * 50) + 1, 48, 48))
        pg.display.update()

    def determineSnake(self,key): #still needs work
        if key in [pg.K_w,pg.K_a,pg.K_s,pg.K_d]:
            return self.snakeList[0]
        else:
            if len(self.snakeList) > 1:
                return self.snakeList[1]

    def determineKeys(self,snake): #needs updating
        index = -1
        for i in range(len(self.snakeList)):
            if self.snakeList[i] == snake:
                index = i
        if index == 0:
            return [pg.K_w,pg.K_d,pg.K_s,pg.K_a]
        else:
            return [pg.K_UP,pg.K_RIGHT,pg.K_DOWN,pg.K_LEFT]