from segment import Segment

class Snake:
    def __init__(self,body=[],out = False):
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
            firstSeg = self.body[0]
            first = Segment(firstSeg.loc,firstSeg.dir) #simulation, what will happen?
            first.setDir(newDir)
            second = self.body[1]
            if first.newLoc() != second.loc:
                self.body[0].setDir(newDir)

    def moveAlong(self, hitApple = False):
        if self.out:
            return
        first = self.body[0]
        if hitApple:
            self.addHead(first)
            return
        self.locations = {}
        self.continueMoving()

    def validMove(self):
        if self.body[0].loc in self.locations:
            self.out = True
            self.body = []
            self.locations = {}
            return False
        return True

    def addHead(self,first):
        self.body.insert(0, Segment(first.newLoc(), first.dir))
        if self.validMove():
            self.locations[self.body[0].loc] = self.body[0]

    def continueMoving(self):
        for i in range(len(self.body)-1, -1, -1): #back to front
            self.body[i].moveSeg()
            if i == 0:
                if not self.validMove():
                    return
            else:
                self.body[i].setDir(self.body[i-1].dir)
            self.locations[self.body[i].loc] = self.body[i]