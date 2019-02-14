from apple_tree import AppleTree
from snake_nest import SnakeNest
import pygame as pg

class Board:
    def __init__(self, rows=0, cols=0, size = 50, numSnakes=1, lengthSnake=3, apples=1):
        self.rows = rows
        self.cols = cols
        self.size = size
        self.screen = pg.display.set_mode((self.cols * self.size, self.rows * self.size))
        #self.apples = AppleTree(apples, rows, cols)
        self.snakes = SnakeNest(self.screen, self.size, numSnakes, lengthSnake, rows, cols)
