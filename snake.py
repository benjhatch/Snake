from segment import Segment
import pygame as pg

class Snake:
    def __init__(self, screen, size, body=[], rows=15, cols=15, color=(0,255,0), out=False):
        self.screen = screen
        self.size = size
        self.rows = rows - 1
        self.cols = cols - 1
        self.color = color
        self.body = body
        self.out = out
        self.locations = {}
        for seg in self.body:
            self.locations[seg.loc] = seg

    def __repr__(self):
        output = ""
        for segment in self.body:
            output += "S" + segment.__repr__() + str(segment.dir) + "*"
        return output

    def changeDir(self,newDir):
        if not self.out:
            first = self.body[0]
            dir = first.dir
            first.setDir(newDir)
            second = self.body[1]
            if first.newLoc() != second.loc:
                self.body[0].setDir(newDir)
                return
            first.setDir(dir)

    def moveAlong(self, hitApple = False):
        if self.out:
            return
        first = self.body[0]
        if hitApple:
            self.addHead(first)
        self.locations = {}
        self.moveBody(hitApple)


    def moveBody(self, hitApple = False):
        for i in range(len(self.body)-1, -1, -1): #back to front
            segment = self.body[i]
            if not hitApple:
                segment.moveSeg()
            if i == 0:
                if not self.validMove():
                    return
            else:
                segment.setDir(self.body[i-1].dir)
            self.locations[segment.loc] = segment
            size = self.size
            pg.draw.rect(self.screen, self.color, ((segment.loc[1] * size) + 1, (segment.loc[0] * size) + 1, size - 2, size - 2))

    def validMove(self):
        firstSeg = self.body[0].loc
        if firstSeg in self.locations:
            self.clear()
            return False
        elif firstSeg[0] < 0 or firstSeg[1] < 0 or firstSeg[0] > self.rows or firstSeg[1] > self.cols:
            self.clear()
            return False
        return True

    def clear(self):
        self.out = True
        self.body = []
        self.locations = {}

    def addHead(self,first):
        body = self.body
        body.insert(0, Segment(first.newLoc(), first.dir))
        if self.validMove():
            self.locations[body[0].loc] = body[0]
            pg.draw.rect(self.screen, self.color, ((body[0].loc[1] * self.size) + 1, (body[0].loc[0] * self.size) + 1, self.size - 2, self.size - 2))

