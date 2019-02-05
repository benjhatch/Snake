from snake import Snake
from segment import Segment
from apple import Apple
import random
import pygame as pg

class Board:
    def __init__(self,rows = 0, cols = 0, numSnakes = 1, length = 3, apples = 1):
        self.rows = rows
        self.cols = cols
        self.grid = self.makeGrid()
        self.snakeList = self.makeSnakes(numSnakes,length)
        self.snakeLocations = [snake.locations for snake in self.snakeList if not snake.out]
        self.appleList = []
        self.appleLocations = [apple.loc for apple in self.appleList]
        self.locations = self.getBadLocations()
        self.appleList = self.makeTree(apples)

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

    def makeGrid(self):
        grid = []
        for r in range(self.rows):
            grid.append([])
            for c in range(self.cols):
                grid[r].append("+")
        return grid

    def getBadLocations(self): #definitely should make this more efficient
        return self.snakeLocations + self.appleLocations #thats a bit better

    def makeTree(self,num):
        list = []
        for j in range(num):
            list.append(Apple("A"))
            if len(self.locations) > 0:
                list[j].changeLoc(self.grid,self.getBadLocations())
            else:
                list[j].changeLoc(self.grid, self.getBadLocations())
        return list


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

    def findApple(self,loc):
        for i in range(len(self.appleList)):
            if self.appleList[i].loc == loc:
                return i

    def moveSnakes(self):
        for i in range(len(self.snakeList)):
            if not self.snakeList[i].out:
                loc = self.snakeList[i].body[0].loc
                if loc not in [apple.loc for apple in self.appleList]:
                    self.snakeList[i].moveAlong(False)
                else:
                    self.snakeList[i].moveAlong(True)
                    #self.appleList[self.findApple(loc)].changeLoc(self.grid,self.getBadLocations())
                self.snakeLocations[i] = self.snakeList[i].locations
                self.checkOutOfBounds(self.snakeList[i])

    def checkOutOfBounds(self, snake):
        firstLoc = snake.body[0].loc
        if (firstLoc[1] > len(self.grid[0]) - 1 or firstLoc[1] < 0) or (firstLoc[0] > len(self.grid) - 1 or firstLoc[0] < 0):
            snake.out = True
            snake.body = []
        elif self.grid[firstLoc[0]][firstLoc[1]] not in ["A", "+"]:
            snake.out = True
            snake.body = []


    def displayGrid(self,screen):
        self.updateInnerGrid()
        screen.fill((0,0,0))
        for apple in self.appleList:
            pg.draw.rect(screen, (255, 0, 0), ((apple.loc[1] * 50) + 1, (apple.loc[0] * 50) + 1, 48, 48))
        for i in range(len(self.snakeList)):
            for segment in self.snakeList[i].body:
                if i == 0:
                    color = (0, 255, 0)
                else:
                    color = (0, 0, 255)
                pg.draw.rect(screen, color, ((segment.loc[1] * 50) + 1, (segment.loc[0] * 50) + 1, 48, 48))
        pg.display.update()

    def updateInnerGrid(self):
        for r in range(self.rows):
            for c in range(self.cols):
                self.grid[r][c] = "+"
        for apple in self.appleList:
            self.grid[apple.loc[0]][apple.loc[1]] = apple.symbol
        for snake in self.snakeList:
            if not snake.out:
                for segment in snake.body:
                    self.grid[segment.loc[0]][segment.loc[1]] = segment.symbol

    def printGrid(self):
        self.updateInnerGrid()
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                print(self.grid[r][c], end="")
            print()