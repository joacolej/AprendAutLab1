# DEPENDENCIES ------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
import os
import sys
import numpy as np
from termcolor import colored

import const
from board import Board


# GAME CLASS --------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

class Game():

    # CONSTRUCTOR ---------------------------------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------------------------------------------------------

    def __init__(self):

        self._boards = []

    # METHODS -------------------------------------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------------------------------------------------------

    def play(self, mode, isPlaying, player):

        b = Board()

        while True:

            if isPlaying or mode == 3:
                self.printBoard(b)

            (x, y) = (0, 0)
            res = False

            while not res:

                if player != None:
                    (x, y) = player.select_best_play(b, 1)
                else:
                    (x, y) = input("Player 2 - Choose 2 coordinates: ").split(",")
                    (x, y) = (int(x) - 1, int(y) - 1)
                    if x == -1 or y == -1:
                        self.printExit()
                    
                res = b.addToken(x, y, 1)
                if not res and isPlaying or mode == 3:
                    print ("\nInsert validate coordinates!\n")

            if b.win(x,y,1) == True:
                self._boards.append(b._matrix.copy())
                if isPlaying or mode == 3:
                    self.printWin(1)
                return self._boards

            if b.draw() == True:
                self._boards.append(b._matrix.copy())
                if isPlaying or mode == 3:
                    self.printDraw()
                return self._boards

            if isPlaying or mode == 3:
                self.printBoard(b)

            res = False

            while not res:

                if mode == const.VS_RANDOM:
                    x = np.random.randint(1,20)
                    y = np.random.randint(1,20)

                else: 
                    (x, y) = input("Player 2 - Choose 2 coordinates: ").split(",")
                    (x, y) = (int(x) - 1, int(y) - 1)
                    if x == -1 or y == -1:
                        self.printExit()
                    
                res = b.addToken(x, y, 2)
                if not res and isPlaying or mode == 3:
                    print ("\nInsert validate coordinates!\n")

            self._boards.append(b._matrix.copy())

            if b.win(x,y,2) == True:
                if isPlaying or mode == 3:
                    self.printWin(2)
                return self._boards

            if b.draw() == True:
                if isPlaying or mode == 3:
                    self.printDraw()
                return self._boards

            if isPlaying or mode == 3:
                self.printBoard(b)

    # AUXILIAR METHODS --------------------------------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------------------------------------------------

    def printClear(self):

        if os.name == 'nt':
            clear = lambda : os.system('cls')
            clear()
        else:
            clear = lambda : os.system('clear')
            clear()
    def printMenu(self):

        self.printClear()
        print ("###################################################")
        print ("#                                                 #")
        print ("#                   GOMOKU v0.1                   #")
        print ("#                                                 #")
        print ("###################################################")
        print ("")
        print ("1. VS Random")
        print ("2. VS Yourself")
        print ("3. VS Human")
    def printBoard(self,b):

        self.printClear()
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

    def printExit(self):

        print ("")
        print ("Exitting game...")
        print ("")

        sys.exit(0)
    def printWin(self, player):

        print ("")

        if player == 1:
            print ("Player 1 won!")
        else:
            print ("Player 2 won!")

        print ("")
    def printDraw(self):

        print ("")
        print ("Its a draw!")
        print ("")


# MAIN --------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    g = Game()
    
    g.printMenu()
    op = input("Choose an option: ")
    g.play(int(op), True, None)
    