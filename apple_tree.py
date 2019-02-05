from apple import Apple
class AppleTree:
    def __init__(self,numApples = 0, grid = [], appleLocations = []):
        self.numApples = numApples
        self.appleLocations = appleLocations
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.appleTree = []
        for i in range(numApples):
            self.appleTree.append(Apple("A"))
            self.appleTree[-1].changeLoc(self.rows,self.cols,self.appleLocations)
            self.appleLocations.append(self.appleTree[-1].loc)

    def snakeHitApple(self,snake):
        head = snake.body[0].loc
        for i in range(len(self.appleTree)):
            if head == self.appleLocations[i]:
                self.appleTree[i].changeLoc(self.rows,self.cols,self.appleLocations)
                self.appleLocations[i] = self.appleTree[i].loc
                return True
        return False