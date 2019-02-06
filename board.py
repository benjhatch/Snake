from snake import Snake
from segment import Segment
from apple_tree import AppleTree
from snake_nest import SnakeNest
import pygame as pg

class Board:
    def __init__(self,rows=0, cols=0, size = 50, numSnakes=1, lengthSnake=3, apples=1):
        self.rows = rows
        self.cols = cols
        self.size = size
        self.apples = AppleTree(apples, rows, cols)
        self.snakes = SnakeNest(numSnakes, lengthSnake, rows, cols, self.apples)


    def displayGame(self,screen):
        screen.fill((0,0,0))
        size = self.size
        for apple in self.apples.appleTree:
            pg.draw.rect(screen, (255, 0, 0), ((apple.loc[1] * size) + 1, (apple.loc[0] * size) + 1, size-2, size-2))
        for i in range(len(self.snakes.nest)):
            for segment in self.snakes.nest[i].body:
                if i == 0:
                    color = (0, 255, 0)
                else:
                    color = (0, 0, 255)
                pg.draw.rect(screen, color, ((segment.loc[1] * size) + 1, (segment.loc[0] * size) + 1, size-2, size-2))
        pg.display.update()

    def determineSnake(self,key): #still needs work
        if key in [pg.K_w,pg.K_a,pg.K_s,pg.K_d]:
            return self.snakes.nest[0]
        else:
            if len(self.snakes.nest) > 1:
                return self.snakes.nest[1]

    def determineKeys(self,snake): #needs updating
        index = -1
        for i in range(len(self.snakes.nest)):
            if self.snakes.nest[i] == snake:
                index = i
        if index == 0:
            return [pg.K_w,pg.K_d,pg.K_s,pg.K_a]
        else:
            return [pg.K_UP,pg.K_RIGHT,pg.K_DOWN,pg.K_LEFT]

    """
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
                self.checkOut(self.snakeList[i], i)
    """