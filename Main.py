from Board import Board
from Game import Game
import pygame as pg
from MyAI import MyAI


winWidth = 800
winHeight = 800
board = Board(winWidth, winHeight)
game = Game()
myAI = MyAI(game)
turn = -1
counter = 1
reset = False
board.refreshWindow(game.gameArr)
run = True


def wait():
    game.reset()
    while True:
        for read in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if read.type == pg.MOUSEBUTTONUP:
                board.refreshWindow(game.gameArr)
                return True


while run:
    pg.time.delay(50)

    if counter >= 9:
        board.tieScreen()
        reset = True

    if turn == 1:
        aiMove = myAI.getBestMove()
        game.gameArr = aiMove[0]
        board.refreshWindow(game.gameArr)
        counter += 1
        if game.isWin(game.gameArr, turn):
            board.looseScreen()
            pg.time.delay(1000)
            reset = True
        turn *= -1

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONUP:
            if game.playMove(turn, board.getClickedBox(pg.mouse.get_pos())):
                board.refreshWindow(game.gameArr)
                counter += 1
                win = game.isWin(game.gameArr, turn)
                if win:
                    board.winScreen()
                    pg.time.delay(1000)
                    reset = True
                turn *= -1
            if counter > 9:
                board.tieScreen()
                reset = True

    if reset:
        reset = False
        counter = 1
        turn *= -1
        wait()

pg.quit()
