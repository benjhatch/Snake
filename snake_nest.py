from snake import Snake
from segment import Segment
from apple_tree import AppleTree
import random
class SnakeNest:
    def __init__(self, numSnakes=0, length=0, rows=0, columns=0, apples=AppleTree(0)):
        self.rows = rows
        self.columns = columns
        self.nest = self.makeSnakes(numSnakes, length)
        self.snakeLocations = [snake.locations for snake in self.nest if not snake.out]
        self.apples = apples

    def makeSnakes(self,numSnakes, length): #need to update placement
        list = []
        for i in range(numSnakes):
            row = random.randint(length, self.rows - length)
            col = random.randint(length, self.columns - length)
            possibleLoc = [row,col]
            if possibleLoc in list:
                i -= 1
            else:
                dir = self.setDir(possibleLoc[1]) #gives the column the snake head is in, may consider revising
                list.append(Snake([Segment("o",possibleLoc,dir)]))
                for j in range(length-1):
                    possibleLoc = list[i].body[j].priorLoc()
                    list[i].body.append(Segment("o",possibleLoc,dir))
        return list

    def setDir(self,col):
        middle = self.columns // 2
        if col < middle:
            return 1 #right
        else:
            return 3 #left

    def moveSnakes(self):
        for i in range(len(self.nest)): #somewhat working, biased for second
            if self.nest[i].out:
                return
            snake = self.nest[i]
            snake.moveAlong(self.apples.snakeHitApple(snake))
            self.snakeLocations[i] = snake.locations #this is the bias, make a new locations function
            if self.checkOut(i):
                self.nest.pop(i)
                break

    def checkOut(self, snakeIndex): #why is this not killing one snake when it hits another?
        out = False
        snake = self.nest[snakeIndex]
        if len(snake.body) > 0:
            firstLoc = snake.body[0].loc
            if (firstLoc[1] > self.columns - 1 or firstLoc[1] < 0) or (firstLoc[0] > self.columns - 1 or firstLoc[0] < 0):
                out = True
            else:
                for i in range(len(self.snakeLocations)):
                    if firstLoc in self.snakeLocations[i] and i != snakeIndex:
                        out = True
        if out:
            snake.out = True
            snake.body = []
            self.snakeLocations.pop(snakeIndex)
            return out