from segment import Segment

class Snake:
    def __init__(self,body=[],out = False):
        self.body = body
        self.out = out
        self.locations = [seg.loc for seg in body]

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

    def moveAlong(self, hitApple = False, grid = []):
        first = self.body[0]
        self.validMove(grid)
        if hitApple:
            self.body.insert(0,Segment("o",first.newLoc(),first.dir))
            self.locations.append(self.body[0].loc)
        else:
            for i in range(len(self.body)):
                self.body[i].moveSeg()
                self.locations.append(self.body[i].loc)
            for i in range(len(self.body)-1, 0, -1):
                self.body[i].setDir(self.body[i-1].dir)

    def validMove(self, grid = []):
        first = self.body[0]
        firstLoc = first.newLoc()
        avoid = [seg.newLoc() for seg in self.body if seg != first]
        if firstLoc in avoid:
            self.out = True
            self.body = []
            return
        elif len(grid) > 0:
            if (firstLoc[1] > len(grid[0]) - 1 or firstLoc[1] < 0) or (firstLoc[0] > len(grid) - 1 or firstLoc[0] < 0):
                self.out = True
                self.body = []
                return
            if grid[firstLoc[0]][firstLoc[1]] not in ["A", "+"]:
                self.out = True
                self.body = []
                return


    def listLocations(self):
        output = []
        if self.out:
            return output
        for seg in self.body:
            output.append(seg.loc)
        return output, self.body[0].symbol
