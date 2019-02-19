import random
import pygame as pg
class Apple:
    def __init__(self, screen, size, color = (255,0,0), loc = (0,0)):
        self.screen = screen
        self.size = size
        self.color = color
        self.loc = loc

    def __repr__(self):
        return "A{}{}".format(self.loc[0],self.loc[1])

    def changeLoc(self, rows, cols, appleLocations, allSnakeLocations):
        self.loc = (random.randint(0,rows),random.randint(0,cols))
        if self.loc in appleLocations or self.loc in allSnakeLocations:
            appleLocations[self.loc].changeLoc(rows,cols,appleLocations,allSnakeLocations)
        else:
            self.drawApple()

    def drawApple(self):
        loc = self.loc
        size = self.size
        pg.draw.rect(self.screen, self.color, ((loc[1] * size), (loc[0] * size), size - 2, size - 2))