from segment import Segment
import pygame as pg

class Snake:
    def __init__(self, screen, size, allSnakeLocations, tailLocations, body, rows, cols, color=(0,255,0), out=False):
        self.screen = screen
        self.size = size
        self.allSnakeLocations = allSnakeLocations
        self.tailLocations = tailLocations
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
            if len(self.body) == 1:
                first.setDir(newDir)
                return
            if first.newLoc(newDir) != self.body[1].loc:
                first.setDir(newDir)

    #draw and update segment on screen and in lists
    def draw(self, segment, first = False):
        size = self.size
        color = self.color
        self.allSnakeLocations.add(segment.loc)  # once you draw the segment, add its location to allSnakeLocations
        if not first:
            self.ownLocations[segment.loc] = segment
            self.tailLocations.add(segment.loc)
        else:
            color = (255,255,255)
        pg.draw.rect(self.screen, color, ((segment.loc[1] * size), (segment.loc[0] * size), size - 2, size - 2))

    #MOVING THE SNAKE
    def moveAlong(self, hitApple = False): #determines course of action when moveSnakes() is called in jungle
        if self.out: #move to next snake
            return 0
        first = self.body[0]
        if hitApple: #snake has hit the apple
            return self.addHead(first) #return length of snake
        else: #if it doesn't hit the apple, move all the segments
            self.ownLocations = {}
            return self.moveBody() #return length of snake

    def moveBody(self): #moves all segments and returns length of snake
        #just for the first segment, detecting out of bounds first
        firstSegment = self.body[0]
        firstSegment.moveSeg()
        if self.outOfBounds():
            self.clear()
            return len(self.body)
        self.draw(firstSegment, True) #first segment doesn't get added to own locations yet
        #rest of snake segments excluding the snake head
        for i in range(len(self.body) - 1, 0, -1):  # back to front
            segment = self.body[i]
            segment.moveSeg()
            segment.setDir(self.body[i - 1].dir)
            self.draw(segment)
            self.ownLocations[segment.loc] = segment
        #check if snake head is in its own body
        self.validMove()
        return len(self.body)

    def addHead(self,first): #add segment onto front of snake when it hits an apple
        body = self.body
        body.insert(0, Segment(first.newLoc(first.dir), first.dir)) #insert segment at front of snake
        if self.validMove():
            self.draw(body[0], True) #first segment doesn't get added to own locations yet
            for i in range(1, len(body)): #draw rest of snake body after you draw the head
                self.draw(body[i])
        return len(self.body)

    #CHECKING VALIDITY OF SNAKE
    def validMove(self):
        firstSeg = self.body[0]
        if firstSeg.loc in self.ownLocations:
            self.clear()
            return False
        elif self.outOfBounds():
            self.clear()
            return False
        self.ownLocations[firstSeg.loc] = firstSeg #now add first segment in own locations
        return True

    def outOfBounds(self):
        loc = self.body[0].loc
        if loc[0] == -1 or loc[1] == -1 or loc[0] == self.rows or loc[1] == self.cols:
            return True
        return False

    def clear(self): #'delete' the snake from the game
        self.out = True
        for i in range(len(self.body)): #maybe don't discard first, idk
            self.allSnakeLocations.discard(self.body[i].loc)
        self.body = []
        self.ownLocations = {}