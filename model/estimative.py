##Combinacion lineal de los atributos y minimos cuadrados
##N-upla(cant fichas, lineas 2 libres, lineas 2 amenazadas, lineas 2 inutiles,
#        lineas 3 libres, lineas 3 amenazadas, lineas 3 inutiles,
#        lineas 4 libres, lineas 4 amenazadas, lineas 4 inutiles
#        lineas 5)
import numpy as np

class Values():
    def __init__(self):
        self.est_function = ([0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1], [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])
        self.learn_rate = 0.5

    def estimate_value(self, move):
        (b_est_function, w_est_function) = self.est_function
        tot = sum(i[0]*i[1] for i in zip(b_est_function, move[0])) + sum(i[0]*i[1] for i in zip(w_est_function, move[1]))
        return tot

    def assign_train_value(self, boards):
        train_values = []
        (b_last, w_last) = boards[-1]
        if b_last[10] > 0:
            train_values.append((boards[-1], 1))
        elif w_last[10] > 0:
            train_values.append((boards[-1], -1))
        else:
            train_values.append((boards[-1], 0))
        for i in range (0, len(boards)-1):
            train_values.append((boards[i], self.estimate_value(boards[i+1])))
        return train_values

    def update_est_function (self, train_values):
        (b_est_function, w_est_function) = self.est_function
        for ((b_board, w_board), v_train) in train_values:
            for i in range (0, len(b_board)):
                b_est_function[i] = b_est_function[i] + self.learn_rate * (v_train - self.estimate_value((b_board, w_board))) * b_board[i]
                w_est_function[i] = w_est_function[i] + self.learn_rate*(v_train - self.estimate_value((b_board, w_board)))*w_board[i]
        self.est_function = (b_est_function, w_est_function)
        print(self.est_function)

    def select_play(self, board):
        first = True
        copy = board.get_matrix()
        for i in range(0, len(copy)):
            for j in range(0, len(copy[0])):
                if copy[i][j] == 0:
                    if first:
                        ret = (i,j)
                        copy[i][j] = 1
                        first = False
                        value = self.estimate_value(copy)
                        copy[i][j] = 0
                    else:
                        copy[i][j] = 1
                        new_value = self.estimate_value(copy)
                        if new_value > value:
                            value = new_value
                            ret = (i, j)
                        elif new_value == value and np.random.randint(0,20) == 3:
                            ret = (i, j)
                        copy[i][j] = 0
        return ret
