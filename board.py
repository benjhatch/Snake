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
        self.keys = {pg.K_w: (0,0), pg.K_d: (0,1), pg.K_s: (0,2), pg.K_a: (0,3), pg.K_UP: (1,0),
                     pg.K_RIGHT: (1,1), pg.K_DOWN: (1,2), pg.K_LEFT: (1,3)}


    def displayGame(self,screen):
        screen.fill((0,0,0))
        size = self.size
        for apple in self.apples.tree.values():
            pg.draw.rect(screen, (255, 0, 0), ((apple.loc[1] * size) + 1, (apple.loc[0] * size) + 1, size-2, size-2))
        for key in self.snakes.segmentLoc:
            color = (0, 255, 0)
            pg.draw.rect(screen, color, ((key[1] * size) + 1, (key[0] * size) + 1, size-2, size-2))
        pg.display.update()
