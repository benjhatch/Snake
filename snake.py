from segment import Segment
import pygame as pg

class Snake:
    def __init__(self, screen, size, allSnakeLocations, body, rows, cols, color=(0,255,0), out=False):
        self.screen = screen
        self.size = size
        self.allSnakeLocations = allSnakeLocations
        self.body = body
        self.rows = rows
        self.cols = cols
        self.color = color
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

    #draw and update segment on screen and in lists
    def draw(self, segment):
        size = self.size
        pg.draw.rect(self.screen, self.color,((segment.loc[1] * size), (segment.loc[0] * size), size - 2, size - 2))
        self.allSnakeLocations.add(segment.loc)
        self.ownLocations[segment.loc] = segment


    #MOVING THE SNAKE
    def moveAlong(self, hitApple = False):
        if self.out:
            return 0
        first = self.body[0]
        if hitApple:
            return self.addHead(first)
        else:
            self.ownLocations = {}
            return self.moveBody()

    def moveBody(self):
        firstSegment = self.body[0]
        if not self.outOfBounds(firstSegment.newLoc(firstSegment.dir)):
            for i in range(len(self.body) - 1, 0, -1):  # back to front excluding the snake head
                segment = self.body[i]
                segment.moveSeg()
                segment.setDir(self.body[i - 1].dir)
                self.draw(segment)
            firstSegment.moveSeg() #just for the first
            if not self.validMove():
                return 0
            else:
                self.draw(firstSegment)
        return len(self.ownLocations)

    def addHead(self,first):
        body = self.body
        body.insert(0, Segment(first.newLoc(first.dir), first.dir))
        if self.validMove():
            self.ownLocations[body[0].loc] = body[0]
            self.draw(body[0])
            for i in range(1, len(body)):
                self.draw(body[i])
        return len(self.body)

    #CHECKING VALIDITY OF SNAKE
    def validMove(self):
        firstSeg = self.body[0].loc
        if firstSeg in self.ownLocations:
            self.clear()
            return False
        elif self.outOfBounds(firstSeg):
            print("out")
            self.clear()
            return False
        return True

    def outOfBounds(self,loc):
        if loc[0] == -1 or loc[1] == -1 or loc[0] == self.rows or loc[1] == self.cols:
            return True
        return False

    def clear(self):
        self.out = True
        for i in range(len(self.body)): #maybe don't discard first, idk
            self.allSnakeLocations.discard(self.body[i].loc)
        self.body = []
        self.ownLocations = {}