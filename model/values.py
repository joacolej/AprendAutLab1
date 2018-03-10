# Combinacion lineal de los atributos y minimos cuadrados
# N-upla(lineas 2 libres, lineas 2 amenazadas, lineas 2 inutiles,
#        lineas 3 libres, lineas 3 amenazadas, lineas 3 inutiles,
#        lineas 4 libres, lineas 4 amenazadas, lineas 4 inutiles
#        lineas 5)

# MAIN --------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

class Values():

    # CONSTRUCTOR ---------------------------------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    
    def __init__(self):
        self.est_function = ([0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0])
        self.learn_rate = 1

    # GETTERS & SETTERS ---------------------------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    
    def get_est_function(self):
        return self.est_function

    def set_est_function(self, function):
        self.est_function = function

    # METHODS -------------------------------------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------------------------------------------------------
    
    def estimate_value(self, move):
        (b_est_function, w_est_function) = self.est_function
        tot = sum(i[0]*i[1] for i in zip(b_est_function, move[0])) + sum(i[0]*i[1] for i in zip(w_est_function, move[1]))
        return tot

    def assign_train_value(self, boards):
        train_values = []
        for i in range (0, len(boards)-1):
            train_values.append((boards[i], self.estimate_value(boards[i+1])))
        (b_last, w_last) = boards[-1]
        if b_last[10] > 0:
            train_values.append((boards[-1], 1))
        elif w_last[10] > 0:
            train_values.append((boards[-1], -1))
        else:
            train_values.append((boards[-1], 0))
        
        return train_values

    def update_est_function (self, train_values):
        (b_est_function, w_est_function) = self.est_function
        for ((b_board, w_board), v_train) in train_values:
            for i in range (1, len(b_board)):
                b_est_function[i] = b_est_function[i] + self.learn_rate*(v_train - self.estimate_value((b_board, w_board)))*b_board[i]
                w_est_function[i] = w_est_function[i] + self.learn_rate*(v_train - self.estimate_value((b_board, w_board)))*w_board[i]
        self.est_function = (b_est_function, w_est_function)

    def select_play(self, board):
        ret = (-1,-1)
        value = -1000
        copy = board.get_matrix()
        for i in range(0, len(copy)):
            for j in range(0, len(copy[0])):
                if copy[i][j] == 0:
                    copy[i][j] = 1
                    new_value = self.estimate_value(copy)
                    if new_value >= value:
                        value = new_value
                        ret = (i, j)
                    copy[i][j] = 0
        return ret
