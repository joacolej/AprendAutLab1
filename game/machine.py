import os
from numpy import random
from termcolor import colored
import sys

def printClear():

    if os.name == 'nt':
        clear = lambda : os.system('cls')
        clear()
    else:
        clear = lambda : os.system('clear')
        clear()


def printExit():

    print ("")
    print ("Exitting game...")
    print ("")


def printWin(player):

    print ("")

    if player == 1:
        print ("Player 1 won!")
    else:
        print ("Player 2 won!")

    print ("")


def printBoard(b, game):
    f = open("juego"+str(game),'w')
    f.writelines(["%s\n" % item  for item in b.get_matrix()])

def MvsRandom(b, turn, player, game):
    freecells = b.get_size()
    boards = []
    while True:
        if freecells == 0:
            printBoard(b, game)
            return boards
        res1 = False
        res2 = False
        while not res1:

            if turn == 1:
                (x1, y1) = player.select_play(b)
            else:
                x1 = random.randint(1,20)
                y1 = random.randint(1,20)

            res1 = b.addToken(x1, y1, 1)
        if b.win(x1,y1,1) == True:
            printBoard(b, game)
            return boards

        freecells = freecells - 1
        while not res2:

            if turn == 2:
                (x2, y2) = player.select_play(b)
            else:
                x2 = random.randint(1,20)
                y2 = random.randint(1,20)

            res2 = b.addToken(x2, y2, 2)
        new_matrix = b.get_matrix().copy()
        boards.append(new_matrix)
        if b.win(x2,y2,2):
            printBoard(b, game)
            printWin(2)
            return boards

        freecells = freecells -1
