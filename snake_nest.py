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
        list = []
        for i in range(numSnakes):
            row = random.randint(length, self.rows - length)
            col = random.randint(length, self.columns - length)
            possibleLoc = (row,col)
            if possibleLoc in self.segmentLoc:
                i -= 1
            else:
                dir = self.setDir(possibleLoc[1])  # gives the column the snake head is in, may consider revising
                list.append(Snake([Segment(possibleLoc, dir)]))
                for j in range(length-1):
                    nextLoc = list[i].body[j].priorLoc()
                    list[i].body.append(Segment(nextLoc,dir))
            self.segmentLoc[i] = list[i].locations
        return list

    def setDir(self,col):
        middle = self.columns // 2
        if col < middle:
            return 1 #right
        else:
            return 3 #left

    def advance(self,i = 0):
        snake = self.nest[i]
        if i == len(self.nest) -1:
            snake.moveAlong(self.snakeHitApple(i))
            self.segmentLoc[i] = snake.locations
        else:
            snake.moveAlong(self.snakeHitApple(i))
            self.segmentLoc[i] = snake.locations
            self.advance(i + 1)
        self.checkOut(i)

    def checkOut(self, snakeIndex):
        snake = self.nest[snakeIndex]
        if snake.out:
            return
        if len(snake.body) > 0:
            firstLoc = snake.body[0].loc
            if (firstLoc[1] > self.columns - 1 or firstLoc[1] < 0) or (firstLoc[0] > self.columns - 1 or firstLoc[0] < 0):
                self.clear(snake)
                return
            else:
                for i in range(len(self.nest)):
                    if i != snakeIndex and firstLoc in self.segmentLoc[i]:
                        self.clear(snake)
                        return

    def clear(self, snake):
        snake.out = True
        snake.body = []
        snake.locations = {}

    def snakeHitApple(self, i): #may need to update placement of apple upon hit and error thrown
        if self.nest[i].out:
            return False
        apples = self.apples
        head = (self.nest[i].body[0].loc[0],self.nest[i].body[0].loc[1])
        if head in apples.tree:
            loc = apples.tree[head].changeLoc(self.rows,self.columns,apples.tree)
            apples.tree[loc] = apples.tree.pop(head)
            return True
        return False