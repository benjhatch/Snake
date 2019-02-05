from apple import Apple
class AppleTree:
    def __init__(self,numApples = 0, rows = 15, cols = 15, appleLocations = []):
        self.numApples = numApples
        self.appleLocations = appleLocations
        self.rows = rows
        self.cols = cols
        self.appleTree = []
        for i in range(numApples):
            self.appleTree.append(Apple("A"))
            self.appleTree[-1].changeLoc(self.rows,self.cols,self.appleLocations)
            self.appleLocations.append(self.appleTree[-1].loc)