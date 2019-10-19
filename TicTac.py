import pygame as pg
import os
import random

pg.init()
pg.font.init()
myFont = pg.font.SysFont('Comic Sans MS', 30)


class Board:
    def __init__(self, width, height):
        self.winWidth = width
        self.winHeight = height
        self.win = pg.display.set_mode((self.winWidth, self.winHeight))
        self.resize = 30
        self.ex = pg.transform.scale(pg.image.load(os.path.join('images', 'X.png')),
                                     ((self.winWidth // 3) - self.resize, (self.winHeight // 3) - self.resize))
        self.oo = pg.transform.scale(pg.image.load(os.path.join('images', 'O.png')),
                                     ((self.winWidth // 3) - self.resize, (self.winHeight // 3) - self.resize))
        pg.mouse.set_visible(1)
        pg.display.set_caption("Tic Tac")

    def refreshWindow(self, positions=None):
        if positions is None:
            positions = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.win.fill((0, 0, 0))
        for i in range(3):
            for j in range(3):
                grid = (
                    j * self.winWidth // 3, i * self.winHeight // 3, self.winWidth // 3 - 1, self.winHeight // 3 - 1)
                pg.draw.rect(self.win, (200, 200, 200), grid, 1)
                if positions[i][j] == -1:
                    self.win.blit(self.ex, (
                        ((j * self.winWidth // 3) + self.resize / 2), ((i * self.winHeight // 3) + self.resize / 2)))
                elif positions[i][j] == 1:
                    self.win.blit(self.oo, (
                        ((j * self.winWidth // 3) + self.resize / 2), ((i * self.winHeight // 3) + self.resize / 2)))
        pg.display.update()

    def getClickedBox(self, pos):
        if pos[0] < self.winWidth // 3 and pos[1] < self.winHeight // 3:
            return [0, 0]
        elif pos[0] < (self.winWidth * 2) // 3 and pos[1] < self.winHeight // 3:
            return [0, 1]
        elif pos[0] < self.winWidth and pos[1] < self.winHeight // 3:
            return [0, 2]
        elif pos[0] < self.winWidth // 3 and pos[1] < (self.winHeight * 2) // 3:
            return [1, 0]
        elif pos[0] < (self.winWidth * 2) // 3 and pos[1] < (self.winHeight * 2) // 3:
            return [1, 1]
        elif pos[0] < self.winWidth and pos[1] < (self.winHeight * 2) // 3:
            return [1, 2]
        elif pos[0] < self.winWidth // 3 and pos[1] < self.winHeight:
            return [2, 0]
        elif pos[0] < (self.winWidth * 2) // 3 and pos[1] < self.winHeight:
            return [2, 1]
        elif pos[0] < self.winWidth and pos[1] < self.winHeight:
            return [2, 2]

    def winScreen(self):
        font = pg.font.Font(None, 70)
        text = font.render("You won :)", True, (50, 50, 50))
        text_rect = text.get_rect(center=(self.winWidth / 2, self.winHeight / 2))
        self.win.blit(text, text_rect)
        pg.display.update()

    def looseScreen(self):
        font = pg.font.Font(None, 70)
        text = font.render("You lost :(", True, (255, 255, 255), (0, 0, 0))
        text_rect = text.get_rect(center=(self.winWidth / 2, self.winHeight / 2))
        self.win.blit(text, text_rect)
        pg.display.update()

    def tieScreen(self):
        font = pg.font.Font(None, 70)
        text = font.render("Tied... -_-", True, (255, 255, 255), (0, 0, 0))
        text_rect = text.get_rect(center=(self.winWidth / 2, self.winHeight / 2))
        self.win.blit(text, text_rect)
        pg.display.update()


class Game:
    def __init__(self):
        self.gameArr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def playMove(self, move, pos):
        if not (self.gameArr[pos[0]][pos[1]] == 1 or self.gameArr[pos[0]][pos[1]] == -1):
            self.gameArr[pos[0]][pos[1]] = move
            return True
        return False

    def reset(self):
        self.gameArr = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def isWin(self, arr, num):
        if self.hasDiagonal(arr, num) or self.hasHorizontal(arr, num) or self.hasVertical(arr, num):
            return True
        return False

    def hasHorizontal(self, arr, num):
        for i in range(3):
            if arr[i][0] == num and arr[i][1] == num and arr[i][2] == num:
                print(arr[i][0], " ", arr[i][1], " ", arr[i][2])
                print("horiz: ", arr)
                return True
        return False

    def hasVertical(self, arr, num):
        for i in range(3):
            if arr[0][i] == num and arr[1][i] == num and arr[2][i] == num:
                print(arr[0][i], " ", arr[1][i], " ", arr[2][i])
                print("ver: ", arr)
                return True
        return False

    def hasDiagonal(self, arr, num):
        if arr[0][0] == num and arr[1][1] == num and arr[2][2] == num:
            print(arr[0][0], " ", arr[1][1], " ", arr[2][2])
            print("dig: ", arr)
            return True
        elif arr[2][0] == num and arr[1][1] == num and arr[0][2] == num:
            print(arr[2][0], " ", arr[1][1], " ", arr[0][2])
            print("dig: ", arr)
            return True
        return False


game = Game()


class MyAI:
    def __init__(self):
        pass

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
        return self.firstMax(self.getVals([game.gameArr]))

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
        if game.isWin(temp[0], -1):
            temp[1] = [-1]
            return temp
        elif game.isWin(temp[0], 1):
            temp[1] = [1]
            return temp
        else:
            maxchildren = []
            count = 0
            for i in range(len(temp[0])):
                for j in range(len(temp[0][i])):
                    if temp[0][i][j] == 0:
                        count += 1
                        print("move max on ", temp)
                        r = self.min(self.doMove(temp, [i, j], 1))
                        print("min returned: ", r)
                        maxchildren.append(r)
            if count == 0:
                temp[1] = [0]
                return temp
            largest = maxchildren[0][1][0]
            temp = maxchildren[0]
            print("children: ", maxchildren)
            for i in range(1, len(maxchildren)):
                if maxchildren[i][1][0] >= largest:
                    if maxchildren[i][1][0] > largest:
                        largest = maxchildren[i][1][0]
                        temp = maxchildren[i]
                    else:
                        rand = random.randint(0, 10)
                        if rand <= 10 / i:
                            print("random: ", rand)
                            largest = maxchildren[i][1][0]
                            temp = maxchildren[i]
            print("Move chosed: ", temp)
            return temp

    def min(self, arr):
        temp = self.getVals(arr)
        if game.isWin(temp[0], -1):
            temp[1] = [-1]
            return temp
        elif game.isWin(temp[0], 1):
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
        if game.isWin(temp[0], -1):
            temp[1] = [-1]
            return temp
        elif game.isWin(temp[0], 1):
            temp[1] = [1]
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


turn = -1
counter = 1
b = Board(700, 700)
run = True
reset = False
b.refreshWindow(game.gameArr)
ai = MyAI()


def wait():
    game.reset()
    while True:
        for read in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if read.type == pg.MOUSEBUTTONUP:
                b.refreshWindow(game.gameArr)
                return True


while run:
    pg.time.delay(50)
    if turn == 1:
        aiMove = ai.getBestMove()
        game.gameArr = aiMove[0]
        b.refreshWindow(game.gameArr)
        counter += 1
        if game.isWin(game.gameArr, turn):
            b.looseScreen()
            pg.time.delay(1000)
            reset = True
        turn *= -1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONUP:
            if game.playMove(turn, b.getClickedBox(pg.mouse.get_pos())):
                b.refreshWindow(game.gameArr)
                counter += 1
                print(counter)
                win = game.isWin(game.gameArr, turn)
                if win:
                    b.winScreen()
                    pg.time.delay(1000)
                    reset = True
                turn *= -1
            if counter > 9:
                b.tieScreen()
                reset = True
    if reset:
        reset = False
        counter = 1
        wait()

pg.quit()
