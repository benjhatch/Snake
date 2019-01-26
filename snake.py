from segment import Segment

class Snake:
    def __init__(self,body=[],out = False):
        self.body = body
        self.out = out

    def __repr__(self):
        output = ""
        for segment in self.body:
            output += segment.symbol + segment.__repr__() + str(segment.dir) + "*"
        return output

    def changeDir(self,newDir):
        if not self.out:
            firstSeg = self.body[0]
            first = Segment("S",firstSeg.loc,firstSeg.dir) #simulation, what will happen?
            first.setDir(newDir)
            second = self.body[1]
            if first.newLoc() != second.loc:
                self.body[0].setDir(newDir)

    def moveAlong(self,hitApple = False):
        first = self.body[0]
        """
        if first.newLoc() in [seg.newLoc() for seg in self.body if seg != first]:
            self.out = True
            self.body = []
        """
        if hitApple:
            self.body.insert(0,Segment("o",first.newLoc(),first.dir))
        else:
            for seg in self.body:
                seg.moveSeg()
            for i in range(len(self.body)-1, 0, -1):
                self.body[i].setDir(self.body[i-1].dir)

    def listLocations(self):
        output = []
        for seg in self.body:
            output.append(seg.loc)
        return output, self.body[0].symbol
