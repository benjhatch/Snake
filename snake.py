from segment import Segment

class Snake:
    def __init__(self,body=[],out = False):
        self.body = body
        self.out = out
        self.locations = [seg.loc for seg in body]

    def __repr__(self):
        output = ""
        for segment in self.body:
            output += "S" + segment.__repr__() + str(segment.dir) + "*"
        return output

    def changeDir(self,newDir):
        if not self.out:
            firstSeg = self.body[0]
            first = Segment("S",firstSeg.loc,firstSeg.dir) #simulation, what will happen?
            first.setDir(newDir)
            second = self.body[1]
            if first.newLoc() != second.loc:
                self.body[0].setDir(newDir)

    def moveAlong(self, hitApple = False):
        if self.out:
            return
        first = self.body[0]
        if hitApple:
            self.body.insert(0,Segment("o",first.newLoc(),first.dir))
            self.locations.insert(0, self.body[0].loc)
        else:
            for i in range(len(self.body)):
                self.body[i].moveSeg()
                if i > len(self.locations) - 1:
                    self.locations.insert(i,self.body[i].loc)
                else:
                    self.locations[i] = self.body[i].loc
            for i in range(len(self.body)-1, 0, -1):
                self.body[i].setDir(self.body[i-1].dir)
        self.validMove()

    def validMove(self):
        first = self.body[0]
        firstLoc = first.loc
        if firstLoc in self.locations[1:]:
            self.out = True
            self.body = []