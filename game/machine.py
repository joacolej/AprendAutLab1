import os
from numpy import random
from termcolor import colored

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


def printBoard(b):

    printClear()
    print ("")

    print("    01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19")

    for x in range(0, 19):

        if x < 9:
            print(" 0", end="")
        else:
            print(" ", end="")
        print(x+1, end=" ")

        for y in range(0,19):
            if b._matrix[x][y] == 0:
                print("[ ]", end="")
            elif b._matrix[x][y] == 1:
                print(colored('[X]', 'blue'), end="")
            elif b._matrix[x][y] == 2:
                print(colored('[O]', 'red'), end="")

        print ("")

    print ("")




def MvsRandom(b, turn, player):
    freecells = b.get_size()
    boards = []
    while True:
        if freecells == 0:
            return boards
        res1 = False
        res2 = False
        printBoard(b)
        while not res1:

            if turn == 1:
                (x1, y1) = player.select_play(b)
            else:
                x1 = random.randint(1,20)
                y1 = random.randint(1,20)

            res1 = b.addToken(x1, y1, 1)
        if b.win(x1,y1,1) == True:
            printWin(1)
            return boards

        freecells = freecells - 1
        printBoard(b)
        while not res2:

            if turn == 2:
                (x2, y2) = player.select_play(b)
            else:
                x2 = random.randint(1,20)
                y2 = random.randint(1,20)

            res2 = b.addToken(x2, y2, 2)
            if not res2:
                print ("\nInsert validate coordinates!\n")
        boards.append(b)
        if b.win(x2,y2,2):
            printWin(2)
            return boards

        freecells = freecells -1
