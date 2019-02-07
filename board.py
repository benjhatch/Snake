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
        for apple in self.apples.tree.values():
            pg.draw.rect(screen, (255, 0, 0), ((apple.loc[1] * size) + 1, (apple.loc[0] * size) + 1, size-2, size-2))
        for key in self.snakes.segmentLoc:
            color = (0, 255, 0)
            pg.draw.rect(screen, color, ((key[1] * size) + 1, (key[0] * size) + 1, size-2, size-2))
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
