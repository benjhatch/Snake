from segment import Segment
import pygame as pg

class Snake:
    def __init__(self, screen, size, allSnakeLocations, body=[], rows=15, cols=15, color=(0,255,0), out=False):
        self.screen = screen
        self.size = size
        self.allSnakeLocations = allSnakeLocations
        self.rows = rows - 1
        self.cols = cols - 1
        self.color = color
        self.body = body
        self.out = out
        self.ownLocations = {}
        for seg in self.body:
            self.ownLocations[seg.loc] = seg

    def __repr__(self):
        output = ""
        for segment in self.body:
            output += "S" + segment.__repr__() + str(segment.dir) + "*"
        return output

    #change snake direction
    def changeDir(self,newDir):
        if not self.out:
            first = self.body[0]
            if first.newLoc(newDir) != self.body[1].loc:
                first.setDir(newDir)

    #draw snake
    def draw(self, segment):
        size = self.size
        pg.draw.rect(self.screen, self.color,((segment.loc[1] * size), (segment.loc[0] * size), size - 2, size - 2))


    #MOVING THE SNAKE
    def moveAlong(self, hitApple = False):
        if self.out:
            self.clear()
            return 0
        first = self.body[0]
        if hitApple:
            self.addHead(first)
        self.ownLocations = {}
        return self.moveBody(hitApple)


    def moveBody(self, hitApple = False):
        lengthOfSnake = 0
        for i in range(len(self.body)-1, -1, -1): #back to front
            segment = self.body[i]
            if not hitApple:
                segment.moveSeg()
            if i == 0:
                if not self.validMove():
                    return 0
            else:
                segment.setDir(self.body[i-1].dir)
            self.ownLocations[segment.loc] = segment
            self.allSnakeLocations.add(segment.loc) #adding location to jungle
            self.draw(segment)
            lengthOfSnake += 1
        return lengthOfSnake

    def validMove(self):
        firstSeg = self.body[0].loc
        if firstSeg in self.ownLocations:
            self.clear()
            return False
        elif firstSeg[0] == 0 or firstSeg[1] == 0 or firstSeg[0] == self.rows or firstSeg[1] == self.cols:
            print("out")
            self.clear()
            return False
        return True

    def clear(self):
        self.out = True
        for i in range(len(self.body)): #maybe don't discard first, idk
            self.allSnakeLocations.discard(self.body[i].loc)
        self.body = []
        self.ownLocations = {}


    def addHead(self,first):
        body = self.body
        body.insert(0, Segment(first.newLoc(first.dir), first.dir))
        if self.validMove():
            self.ownLocations[body[0].loc] = body[0]
            self.draw(body[0])