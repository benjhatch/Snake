from snake import Snake
from segment import Segment
from apple import Apple
import pygame as pg
import random
class Jungle:
    def __init__(self):
        self.colorList = [(0, 255, 0), (0, 0, 255), (255, 255, 255), (100, 100, 150), (30, 100, 180)]
        #lists
        self.allSnakeLocations = set()  # keeps track of all snake locations in one list
        self.tailLocations = set()

        self.getJungleSettings()
        self.keys = {pg.K_w: (0, 0), pg.K_d: (0, 1), pg.K_s: (0, 2), pg.K_a: (0, 3), pg.K_UP: (1, 0),
                     pg.K_RIGHT: (1, 1), pg.K_DOWN: (1, 2), pg.K_LEFT: (1, 3),
                     pg.K_i: (2, 0), pg.K_l: (2, 1), pg.K_k: (2, 2), pg.K_j: (2, 3)}

    #JUNGLE IN ACTION
    def moveSnakes(self): #moves all snakes
        self.allSnakeLocations.clear() #clear prior moves locations
        self.tailLocations.clear()
        applesToBeMoved = [] #keeps track of which apples are hit
        lengthOfAllSnakes = 0
        appleHit = False
        for i in range(len(self.snakes)): #for all snakes
            snake = self.snakes[i]
            lengthOfAllSnakes += snake.moveAlong() #returns length of snake and moves it
            if self.detectHit(snake,applesToBeMoved): #detects if snake hits any apple
                appleHit = True
        if appleHit:
            self.moveApples(applesToBeMoved) #moves the apples that are hit
        self.drawApples() #draws the apples
        if len(self.allSnakeLocations) < lengthOfAllSnakes: #this means a snake has hit another snake
            self.snakeCollision() #handle snake collision

    def detectHit(self, snake, applesToBeMoved):
        if not snake.out and snake.body[0].loc in self.apples:
            snake.toBeAdded += self.toBeAdded
            applesToBeMoved.append(self.apples[snake.body[0].loc])
            return True
        return False

    def moveApples(self, applesToBeMoved):
        for i in range(len(applesToBeMoved)):
            self.apples.pop(applesToBeMoved[i].loc)
            applesToBeMoved[i].changeLoc(self.rows, self.cols, self.apples, self.allSnakeLocations)
            self.apples[applesToBeMoved[i].loc] = applesToBeMoved[i]

    def drawApples(self):
        for location in self.apples:
            self.apples[location].drawApple()

    def snakeCollision(self):
        toBeCleared = []
        snakeHeads = [snake.body[0].loc for snake in self.snakes if not snake.out]
        for i in range(len(self.snakes)):
            snake = self.snakes[i]
            if not snake.out:
                loc = snake.body[0].loc
                if loc in self.tailLocations or snakeHeads.count(loc) > 1:
                    toBeCleared.append(i)
        for i in range(len(toBeCleared)):
            self.snakes[toBeCleared[i]].clear()

    #INITIALIZING JUNGLE
    #settings
    def getJungleSettings(self):
        default = input("Default Settings? 'y' for yes or 'n' for no: ")
        if default == 'y':
            self.rows = 40
            self.cols = 40
            self.blockSize = 10
            self.screen = pg.display.set_mode(((self.cols) * self.blockSize, (self.rows) * self.blockSize))
            self.toBeAdded = 5
            self.snakes = self.initSnakes(1, 5)
            self.apples = self.initApples(1)
        else:
            self.rows = int(input("Enter number of rows: "))
            self.cols = int(input("Enter number of columns: "))
            self.blockSize = int(input("Enter segment size: "))
            #prepare to make snake and apple lists
            numSnakes = int(input("Enter number of snakes: "))
            length = int(input("Enter snake length: "))
            numApples = int(input("Enter number of apples: "))
            self.toBeAdded = int(input("Enter snake gain upon apple contact: "))
            self.screen = pg.display.set_mode(((self.cols) * self.blockSize, (self.rows) * self.blockSize))
            self.snakes = self.initSnakes(numSnakes, length)
            self.apples = self.initApples(numApples)

    #snake making
    def initSnakes(self, count, length):
        snakes = []
        for i in range(count):
            row = random.randint(length, self.rows - 1)
            col = self.placeFirstPeice(length)
            dir = self.initDir(col)
            snakes.append(Snake(self.screen, self.blockSize, self.allSnakeLocations, self.tailLocations, [Segment((row, col), dir)], self.rows, self.cols, self.colorList[i]))
            self.allSnakeLocations.add((row,col))
            for j in range(length - 1):  # adding on rest of segments
                nextLocation = snakes[i].body[j].priorLoc(dir)
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

    # apple making
    def initApples(self, numApples):
        apples = {}
        for i in range(numApples):
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if (row, col) in apples or (row, col) in self.allSnakeLocations:
                i -= 1
            else:
                apples[(row, col)] = Apple(self.screen, self.blockSize, (row, col))
        return apples