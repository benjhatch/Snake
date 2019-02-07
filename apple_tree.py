from apple import Apple
class AppleTree:
    def __init__(self,numApples = 0,rows = 15, cols = 15):
        self.tree = {}
        for i in range(numApples):
            apple = Apple()
            apple.changeLoc(rows,cols,self.tree)
            self.tree[apple.loc] = apple