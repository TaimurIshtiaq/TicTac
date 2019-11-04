import pygame as pg
import os

pg.init()
pg.font.init()


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
        pg.display.set_caption("Tic Tac Toe")

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
        font = pg.font.Font(None, 100)
        text = font.render("You won :)", True, (255, 255, 255),  (0, 0, 0))
        text_rect = text.get_rect(center=(self.winWidth // 2, self.winHeight // 2))
        self.win.blit(text, text_rect)
        pg.display.update()

    def looseScreen(self):
        font = pg.font.Font(None, 100)
        text = font.render("You lost :(", True, (255, 255, 255), (0, 0, 0))
        text_rect = text.get_rect(center=(self.winWidth // 2, self.winHeight // 2))
        self.win.blit(text, text_rect)
        pg.display.update()

    def tieScreen(self):
        font = pg.font.Font(None, 100)
        text = font.render("Tied... -_-", True, (255, 255, 255), (0, 0, 0))
        text_rect = text.get_rect(center=(self.winWidth // 2, self.winHeight // 2))
        self.win.blit(text, text_rect)
        pg.display.update()


