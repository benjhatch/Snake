import random
class Apple:
    def __init__(self, loc = (0,0)):
        self.loc = loc

    def __repr__(self):
        return "A{}{}".format(self.loc[0],self.loc[1])

    def changeLoc(self,rows,cols,locations):
        self.loc = (random.randint(0,rows-1),random.randint(0,cols-1))
        if self.loc in locations:
            locations[self.loc].changeLoc(rows,cols,locations)
        return self.loc