import random

class MyAI:
    def __init__(self, game):
        self.game = game

    def getVals(self, arr):
        temp = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
        for i in range(len(arr[0])):
            for j in range(len(arr[0][i])):
                temp[0][i][j] = arr[0][i][j]
        try:
            temp.append(arr[1])
            return temp
        except:
            temp.append([None])
            return temp

    def getBestMove(self):
        return self.firstMax(self.getVals([self.game.gameArr]))

    def doMove(self, arr, pos, who):
        temp = self.getVals(arr)
        temp[0][pos[0]][pos[1]] = who
        return temp

    def firstMax(self, arr):
        temp = self.getVals(arr)
        notEmpty = False
        for i in range(len(temp[0])):
            for j in range(len(temp[0][0])):
                if not temp[0][i][j] == 0:
                    notEmpty = True
                    break
        if not notEmpty:
            return self.doMove(temp, [1, 1], 1)
        if self.game.isWin(temp[0], -1):
            temp[1] = [-1]
            return temp
        else:
            maxChildren = []
            count = 0
            for i in range(len(temp[0])):
                for j in range(len(temp[0][i])):
                    if temp[0][i][j] == 0:
                        count += 1
                        print("move max on ", temp)
                        r = self.min(self.doMove(temp, [i, j], 1))
                        print("min returned: ", r)
                        maxChildren.append(r)
            if count == 0:
                temp[1] = [0]
                return temp
            largest = maxChildren[0][1][0]
            temp = maxChildren[0]
            print("children: ", maxChildren)
            for i in range(1, len(maxChildren)):
                if maxChildren[i][1][0] >= largest:
                    if maxChildren[i][1][0] > largest:
                        largest = maxChildren[i][1][0]
                        temp = maxChildren[i]
                    else:
                        rand = random.randint(0, 10)
                        if rand <= 10 / i:
                            print("random: ", rand)
                            largest = maxChildren[i][1][0]
                            temp = maxChildren[i]
            print("Move chosen: ", temp)
            return temp

    def min(self, arr):
        temp = self.getVals(arr)
        if self.game.isWin(temp[0], 1):
            temp[1] = [1]
            return temp
        else:
            children = []
            count = 0
            for i in range(len(temp[0])):
                for j in range(len(temp[0][i])):
                    if temp[0][i][j] == 0:
                        count += 1
                        print("move min on ", temp)
                        r = self.max(self.doMove(temp, [i, j], -1))
                        print("max returned: ", r)
                        children.append(r)
            if count == 0:
                temp[1] = [0]
                return temp
            smallest = children[0][1][0]
            print("children: ", children)
            for i in range(1, len(children)):
                if children[i][1][0] < smallest:
                    smallest = children[i][1][0]
            temp[1] = [smallest]
            return temp

    def max(self, arr):
        temp = self.getVals(arr)
        if self.game.isWin(temp[0], -1):
            temp[1] = [-1]
            return temp
        else:
            children = []
            count = 0
            for i in range(len(temp[0])):
                for j in range(len(temp[0][i])):
                    if temp[0][i][j] == 0:
                        count += 1
                        print("move MAX on ", temp)
                        r = self.min(self.doMove(temp, [i, j], 1))
                        print("min returned: ", r)
                        children.append(r)
            if count == 0:
                temp[1] = [0]
                return temp
            largest = children[0][1][0]
            for i in range(len(children)):
                if children[i][1][0] > largest:
                    largest = children[i][1][0]
            temp[1] = [largest]
            return temp
