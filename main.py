# DEPENDENCIES ------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
import os
import sys
from game.board import Board
from termcolor import colored
from numpy import random
from model.estimative import Values
from game.machine import MvsRandom
from model.matrix import matrix_to_values
# AUXILIAR METHODS --------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

def printClear():

    if os.name == 'nt':
        clear = lambda : os.system('cls')
        clear()
    else:
        clear = lambda : os.system('clear')
        clear()

def printMenu():

    printClear()
    print ("###################################################")
    print ("#                                                 #")
    print ("#                   GOMOKU v0.1                   #")
    print ("#                                                 #")
    print ("###################################################")
    print ("")
    print ("1. VS Random")
    print ("2. VS Yourself")
    print ("3. VS Human")
    print ("4. Machine VS Random")

def printExit():

    print ("")
    print ("Exitting game...")
    print ("")

    sys.exit(0)

def printWin(player):

    print ("")

    if player == 1:
        print ("Player 1 won!")
    else:
        print ("Player 2 won!")

    print ("")

    sys.exit(0)

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

# GAME MODE METHODS -------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

def vsRandom(b, turn):

    while True:

        printBoard(b)

        (x1, y1) = (0, 0)
        (x2, y2) = (0, 0)

        res1 = False
        res2 = False

        while not res1:

            if turn == 1:
                (x1, y1) = input("Player 1 - Choose 2 coordinates: ").split(",")
                (x1, y1) = (int(x1) - 1, int(y1) - 1)

                if x1 == -1 or y1 == -1:
                    printExit()

            else:
                x1 = random.randint(1,20)
                y1 = random.randint(1,20)

            res1 = b.addToken(x1, y1, 1)
            if not res1:
                print ("\nInsert validate coordinates!\n")

        if b.win(x1,y1,1) == True:
            printWin(1)

        printBoard(b)

        while not res2:

            if turn == 2:
                (x2, y2) = input("Player 2 - Choose 2 coordinates: ").split(",")
                (x2, y2) = (int(x2) - 1, int(y2) - 1)

                if x2 == -1 or y2 == -1:
                    printExit()

            else:
                x2 = random.randint(1,20)
                y2 = random.randint(1,20)

            res2 = b.addToken(x2, y2, 2)
            if not res2:
                print ("\nInsert validate coordinates!\n")

        if b.win(x2,y2,2):
            printWin(2)

def vsMyself(b, turn):

    turnFlag = False

    while True:

        printBoard(b)

        if not turnFlag:
            print ("You are player ", end="")
            print (turn)
            print ("")
            turnFlag = True

        (x1, y1) = (0, 0)
        (x2, y2) = (0, 0)

        res1 = False
        res2 = False

        while not res1:
            (x1, y1) = input("Player 1 - Choose 2 coordinates: ").split(",")
            (x1, y1) = (int(x1) - 1, int(y1) - 1)

            if x1 == -1 or y1 == -1:
                printExit()

            res1 = b.addToken(x1, y1, 1)
            if not res1:
                print ("\nInsert validate coordinates!\n")

        if b.win(x1,y1,1) == True:
            printWin(1)

        printBoard(b)

        while not res2:
            (x2, y2) = input("Player 2 - Choose 2 coordinates: ").split(",")
            (x2, y2) = (int(x2) - 1, int(y2) - 1)

            if x2 == -1 or y2 == -1:
                printExit()

            res2 = b.addToken(x2, y2, 2)
            if not res2:
                print ("\nInsert validate coordinates!\n")

        if b.win(x2,y2,2):
            printWin(2)

def vsHuman(b, turn):

    turnFlag = False

    while True:

        printBoard(b)

        if not turnFlag:
            print ("You are player ", end="")
            print (turn)
            print ("")
            turnFlag = True

        (x1, y1) = (0, 0)
        (x2, y2) = (0, 0)

        res1 = False
        res2 = False

        while not res1:
            (x1, y1) = input("Player 1 - Choose 2 coordinates: ").split(",")
            (x1, y1) = (int(x1) - 1, int(y1) - 1)

            if x1 == -1 or y1 == -1:
                printExit()

            res1 = b.addToken(x1, y1, 1)
            if not res1:
                print ("\nInsert validate coordinates!\n")

        if b.win(x1,y1,1) == True:
            printWin(1)

        printBoard(b)

        while not res2:
            (x2, y2) = input("Player 2 - Choose 2 coordinates: ").split(",")
            (x2, y2) = (int(x2) - 1, int(y2) - 1)

            if x2 == -1 or y2 == -1:
                printExit()

            res2 = b.addToken(x2, y2, 2)
            if not res2:
                print ("\nInsert validate coordinates!\n")

        if b.win(x2,y2,2):
            printWin(2)

# MAIN --------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    printMenu()
    op = input("Choose an option: ")

    b = Board()
    turn = random.randint(1,3)

    if op == "1":
        vsRandom(b, turn)

    if op == "2":
        vsMyself(b, turn)

    if op == "3":
        vsHuman(b, turn)

    if op == "4":
        moves = []
        player = Values()
        for i in range (0,100):
            b = Board()
            boards = MvsRandom(b, turn, player)
            for board in boards:
                moves.append(matrix_to_values(board.get_matrix()))
            train_values = player.assign_train_value(moves)
            player.update_est_function(train_values)
