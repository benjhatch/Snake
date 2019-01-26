class Segment:
    def __init__(self, symbol, loc = [7,7], dir = 1):
        self.symbol = symbol
        self.loc = loc
        self.dir = dir

    def __repr__(self):
        return "[{},{}]".format(self.loc[0],self.loc[1])

    def newLoc(self):
        if self.dir == 0: #up
            return [self.loc[0]-1,self.loc[1]]
        elif self.dir == 1: #right
            return [self.loc[0],self.loc[1]+1]
        elif self.dir == 2: #down
            return [self.loc[0]+1,self.loc[1]]
        elif self.dir == 3: #left
            return [self.loc[0],self.loc[1]-1]

    def priorLoc(self):
        if self.dir == 0: #down
            return [self.loc[0]+1,self.loc[1]]
        elif self.dir == 1: #left
            return [self.loc[0], self.loc[1] - 1]
        elif self.dir == 2: #up
            return [self.loc[0] - 1, self.loc[1]]
        elif self.dir == 3: #right
            return [self.loc[0], self.loc[1] + 1]

    def moveSeg(self):
        self.loc = self.newLoc()

    def setDir(self, newDir):
        self.dir = newDir