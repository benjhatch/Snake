from snake import Snake
from segment import Segment
from apple_tree import AppleTree
import random
class SnakeNest:
    def __init__(self, numSnakes=0, length=0, rows=0, columns=0, apples=AppleTree(0)):
        self.rows = rows
        self.columns = columns
        self.segmentLoc = {}
        self.nest = self.makeSnakes(numSnakes, length)
        self.apples = apples

    def makeSnakes(self,numSnakes, length): #need to update placement
        dic = {}
        for i in range(numSnakes):
            row = random.randint(length, self.rows - length)
            col = random.randint(length, self.columns - length)
            possibleLoc = (row,col)
            if possibleLoc in self.segmentLoc:
                i -= 1
            else:
                dir = self.setDir(possibleLoc[1])  # gives the column the snake head is in, may consider revising
                dic[i] = Snake([Segment(possibleLoc, dir)])
                self.segmentLoc[possibleLoc] = dic[i].body[0].loc
                for j in range(length-1):
                    nextLoc = dic[i].body[j].priorLoc()
                    dic[i].body.append(Segment(nextLoc,dir))
                    self.segmentLoc[nextLoc] = dic[i].body[j+1].loc
        return dic

    def setDir(self,col):
        middle = self.columns // 2
        if col < middle:
            return 1 #right
        else:
            return 3 #left

    def advance(self):
        self.segmentLoc = {}
        self.moveSnakes()

    def moveSnakes(self, index = 0):
        if index == len(self.nest) - 1:
            self.nest[index].moveAlong(self.snakeHitApple(index))
            #self.checkOut(index)
        else:
            self.nest[index].moveAlong(self.snakeHitApple(index))
            self.moveSnakes(index + 1)
            #self.checkOut(index)
        self.segmentLoc.update(self.nest[index].locations)

    def checkOut(self, snakeIndex):
        if self.nest[snakeIndex].out:
            self.snakeLocations.pop(snakeIndex)
            self.nest.pop(snakeIndex)
        out = False
        snake = self.nest[snakeIndex]
        if len(snake.body) > 0:
            firstLoc = snake.body[0].loc
            if (firstLoc[1] > self.columns - 1 or firstLoc[1] < 0) or (firstLoc[0] > self.columns - 1 or firstLoc[0] < 0):
                out = True
            else:
                for i in range(len(self.snakeLocations)):
                    if i == snakeIndex:
                        continue
                    elif firstLoc in self.snakeLocations[i]:
                        out = True
        if out:
            snake.out = True
            snake.body = []

    def snakeHitApple(self, index): #may need to update placement of apple upon hit and error thrown
        if self.nest[index].out:
            return False
        apples = self.apples
        head = (self.nest[index].body[0].loc[0],self.nest[index].body[0].loc[1])
        if head in apples.tree:
            loc = apples.tree[head].changeLoc(self.rows,self.columns,apples.tree)
            apples.tree[loc] = apples.tree.pop(head)
            return True
        return False

"""
        self.rows = rows
        self.columns = columns
        self.nest = self.makeSnakes(numSnakes, length)
        self.snakeLocations = [snake.locations for snake in self.nest if not snake.out]
        self.apples = apples
        
        
        list = []
        for i in range(numSnakes):
            row = random.randint(length, self.rows - length)
            col = random.randint(length, self.columns - length)
            possibleLoc = [row,col]
            if possibleLoc in list:
                i -= 1
            else:
                dir = self.setDir(possibleLoc[1]) #gives the column the snake head is in, may consider revising
                list.append(Snake([Segment(possibleLoc,dir)]))
                for j in range(length-1):
                    possibleLoc = list[i].body[j].priorLoc()
                    list[i].body.append(Segment(possibleLoc,dir))
        return list
"""