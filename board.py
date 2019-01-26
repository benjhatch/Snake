from snake import Snake
from segment import Segment
from apple import Apple
import random
import pygame as pg

class Board:
    def __init__(self,rows = 0, cols = 0, apples = 1):
        self.rows = rows
        self.cols = cols
        self.grid = self.makeGrid()
        self.snakeList = []
        self.appleList = []
        self.locations = self.getBadLocations()
        self.appleList = self.makeTree(apples)

    def makeGrid(self):
        grid = []
        for r in range(self.rows):
            grid.append([])
            for c in range(self.cols):
                grid[r].append("+")
        return grid

    def getBadLocations(self):
        locations = []
        for snake in self.snakeList:
            for segment in snake.body:
                locations.append(segment.loc)
        for apple in self.appleList:
            locations.append(apple.loc)
        return locations

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
        for i in range(numSnakes):
            row = random.randint(length, self.rows - length)
            col = random.randint(length, self.cols - length)
            possibleLoc = [row,col]
            if possibleLoc in self.snakeList:
                i -= 1
            else:
                dir = self.getDir(possibleLoc[1])
                self.snakeList.append(Snake([Segment("o",possibleLoc,dir)]))
                for j in range(length-1):
                    possibleLoc = self.snakeList[i].body[j].priorLoc()
                    self.snakeList[i].body.append(Segment("o",possibleLoc,dir))
        return self.snakeList

    def findApple(self,loc):
        for i in range(len(self.appleList)):
            if self.appleList[i].loc == loc:
                return i
            
    def nextMoveGood(self,snake,index): #check this
        first = snake.body[0].newLoc()
        if (first[1] > self.cols - 1 or first[1] < 0) or (first[0] > self.rows - 1 or first[0] < 0):
            self.snakeList.pop(index)
            return False
        elif self.grid[first[0]][first[1]] not in ["A","+"]: #'A' is for apple
            self.snakeList.pop(index)
            return False
        else:
            return True


    def moveSnakes(self):
        for i in range(len(self.snakeList)):
            if self.nextMoveGood(self.snakeList[i],i): #and check this
                loc = self.snakeList[i].body[0].loc
                if loc not in [apple.loc for apple in self.appleList]:
                    self.snakeList[i].moveAlong()
                else:
                    self.snakeList[i].moveAlong(True)
                    self.appleList[self.findApple(loc)].changeLoc(self.grid,self.getBadLocations())

    def displayGrid(self,screen):
        self.updateInnerGrid()
        screen.fill((0,0,0))
        for apple in self.appleList:
            pg.draw.rect(screen, (255, 0, 0), ((apple.loc[1] * 50) + 1, (apple.loc[0] * 50) + 1, 48, 48))
        for snake in self.snakeList:
            for segment in snake.body:
                pg.draw.rect(screen, (0, 255, 0), ((segment.loc[1] * 50) + 1, (segment.loc[0] * 50) + 1, 48, 48))
        pg.display.update()

    def printGrid(self):
        self.updateInnerGrid()
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                print(self.grid[r][c], end="")
            print()

    def updateInnerGrid(self):
        for r in range(self.rows):
            for c in range(self.cols):
                self.grid[r][c] = "+"
        for apple in self.appleList:
            self.grid[apple.loc[0]][apple.loc[1]] = apple.symbol
        for snake in self.snakeList:
            for segment in snake.body:
                self.grid[segment.loc[0]][segment.loc[1]] = segment.symbol

