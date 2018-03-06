# DEPENDENCIES ------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
import os
import sys
from board import Board
from termcolor import colored

# AUXILIAR METHODS --------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

def printMenu():

    clear = lambda : os.system('clear')
    clear()

    print ("###################################################")
    print ("#                                                 #")
    print ("#                   GOMOKU v0.1                   #")
    print ("#                                                 #")
    print ("###################################################")
    print ("")
    print ("1. VS Random")
    print ("2. VS Yourself")
    print ("3. VS Human")

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

    clear = lambda : os.system('clear')
    clear()

    print ("")

    for x in range(0, 19):
        for y in range(0,19):
            if b._matrix[x][y] == 0:
                print("[ ]", end="")
            elif b._matrix[x][y] == 1:
                print(colored('[X]', 'blue'), end="")
            elif b._matrix[x][y] == 2:
                print(colored('[O]', 'red'), end="")

        print ("")

    print ("")
    
# MAIN --------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    
    printMenu()
    op = input("Choose an option: ")

    if op == "1":

        b = Board()

        while True:

            printBoard(b)

            (x1, y1) = (0, 0)
            (x2, y2) = (0, 0)
            
            res1 = False
            res2 = False

            while not res1:
                (x1, y1) = input("Player 1 - Choose 2 coordinates: ").split(",")
                (x1, y1) = (int(x1), int(y1))
                
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
                (x2, y2) = (int(x2), int(y2))

                if x2 == -1 or y2 == -1:
                    printExit()

                res2 = b.addToken(x2, y2, 2)
                if not res2:
                    print ("")
                    print ("\nInsert validate coordinates!\n")

            if b.win(x2,y2,1):
                printWin(2)

    if op == "2":
        print("2")

    if op == "3":
        print("3")