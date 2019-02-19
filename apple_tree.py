from apple import Apple
class AppleTree:
    def __init__(self, screen, size, rows, cols, allSnakeLocations, numApples = 0, color = (255,0,0)):
        self.screen = screen
        self.size = size
        self.rows = rows - 1
        self.cols = cols -1
        self.allSnakeLocations = allSnakeLocations
        self.appleLocations = {}
        self.apples = []
        self.color = color
        for i in range(numApples):
            apple = Apple(self.screen, self.size, self.color)
            apple.changeLoc(rows, cols, self.appleLocations, self.allSnakeLocations)
            self.appleLocations[apple.loc] = apple
            self.apples.append(apple)

    def appleHit(self,loc):
        apple = self.appleLocations[loc]
        apple.changeLoc(self.rows, self.cols, self.appleLocations, self.allSnakeLocations)
        self.appleLocations.pop(loc)
        self.appleLocations[apple.loc] = apple

    def drawApples(self):
        for apple in self.apples:
            apple.drawApple()