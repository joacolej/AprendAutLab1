import game.board as board
from model.estimative import Values
from matrix_parser import matrix_to_values
from numpy import random

# 1 = IA
# 2 = RANDOM

class Trainer():

    def __init__(self):
        self.ai = Values()

    def play_game (self):
        win = False
        # Lista de moves, empieza el tablero vacio
        moves = [([0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0])]
        b = board.Board()
        while not win:
            (b, win) = self.random_move(b, win)
            moves.append(matrix_to_values(b.getMatrix()))
            if not win:
                # Juega la PC
                b = self.computer_move(b)
                moves.append(matrix_to_values(b.getMatrix()))
        return moves

    def random_move(self, board, win):
        played = False
        x = random.randint(0,19)
        y = random.randint(0,19)
        while not played:
            played = board.addToken(x,y,2)
            if board.win(x,y,2):
                win = True
            if not played:
                x = random.randint(0,19)
                y = random.randint(0,19)
            if win:
                return (board, win)
        return (board, win)

    def computer_move(self, board):
        played = False
        max_play = 0;
        position = (0,0)
        for x in range(0,19):
            for y in range(0,19):
                if board.addToken(x,y,1):
                    board_value = self.ai.estimate_value(matrix_to_values(board.getMatrix()))
                    if board_value > max_play:
                        max_play = board_value
                        position =(x,y)
                    board.removeToken(x,y)
        return board
