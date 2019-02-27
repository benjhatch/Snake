class Segment:
    def __init__(self, loc = (7,7), dir = 1):
        self.loc = loc
        self.dir = dir

    def __repr__(self):
        return "[{},{}]".format(self.loc[0],self.loc[1])

    #MOVING THE SEGMENT
    def moveSeg(self):
        self.loc = self.newLoc(self.dir)

    def setDir(self, newDir):
        self.dir = newDir

    #PREDICTING SEGMENT LOCATION
    def newLoc(self,dir):
        if dir == 0: #up
            return (self.loc[0]-1,self.loc[1])
        elif dir == 1: #right
            return (self.loc[0],self.loc[1]+1)
        elif dir == 2: #down
            return (self.loc[0]+1,self.loc[1])
        elif dir == 3: #left
            return (self.loc[0],self.loc[1]-1)

    def priorLoc(self,dir):
        if dir == 0: #down
            return (self.loc[0]+1,self.loc[1])
        elif dir == 1: #left
            return (self.loc[0], self.loc[1] - 1)
        elif dir == 2: #up
            return (self.loc[0] - 1, self.loc[1])
        elif dir == 3: #right
            return (self.loc[0], self.loc[1] + 1)