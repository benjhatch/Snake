import random
class Apple:
    def __init__(self,symbol,loc = [0,0]):
        self.symbol = symbol
        self.loc = loc

    def __repr__(self):
        return self.symbol + "{}{}".format(self.loc[0],self.loc[1])

    def changeLoc(self,grid,locations):
        self.loc = [random.randint(0,len(grid)-1),random.randint(0,len(grid[0])-1)]
        if self.loc in locations:
            self.changeLoc(grid,locations)