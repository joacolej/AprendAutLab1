##Combinacion lineal de los atributos y minimos cuadrados
##N-upla(cant fichas, lineas 2 libres, lineas 2 amenazadas, lineas 2 inutiles,
#        lineas 3 libres, lineas 3 amenazadas, lineas 3 inutiles,
#        lineas 4 libres, lineas 4 amenazadas, lineas 4 inutiles
#        lineas 5)
class Values():
    def __init__(self):
        # Pesos wi
        self.est_function = ([0,0,0,0,0,0,0,0,0,0,1], [0,0,0,0,0,0,0,0,0,0,0])
        self.learn_rate = 0.5

    def estimate_value(self, move):
        (b_est_function, w_est_function) = self.est_function
        tot = sum(i[0]*i[1] for i in zip(b_est_function, move[0])) + sum(i[0]*i[1] for i in zip(w_est_function, move[1]))
        return tot

    def assign_train_value(self, moves):
        train_values = []
        (b_last, w_last) = moves[-1]
        if b_last[11] > 0:
            train_values.append((moves[-1], 1))
        elif w_last[11] > 0:
            train_values.append((moves[-1], -1))
        else:
            train_values.append((moves[-1], 0))
        for i in range (0, len(moves)-1):
            train_values.append((moves[i]), self.estimate_value(moves[i+1]))
        return train_values

    def update_est_function (self, train_values):
        (b_est_function, w_est_function) = self.est_function
        for ((b_board, w_board), v_train) in train_values:
            for i in range (0, len(b_board)):
                b_est_function[i] = b_est_function[i] + self.learn_rate*(v_train - self.estimate_value((b_board, w_board)))*b_board[i]
                w_est_function[i] = w_est_function[i] + self.learn_rate*(v_train - self.estimate_value((b_board, w_board)))*w_board[i]
        self.est_function = (b_est_function, w_est_function)
