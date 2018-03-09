# DEPENDENCIES ------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
import numpy as np

from .values import Values
from .features import Features

# MAIN --------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

class Player():

    # CONSTRUCTOR ---------------------------------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------------------------------------------------------

    def __init__(self, v, f):

        self.v = v
        self.f = f

    # METHODS -------------------------------------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------------------------------------------------------

    def select_best_play(self, board, turn):

        ret = (-1,-1)

        value = -1000

        for i in range(0, 19):
            for j in range(0, 19):

                if board.addToken(i,j,turn):
                    feature = self.f.get_features(board.get_matrix())
                    new_value = self.v.estimate_value(feature)
                    if new_value > value:
                        value = new_value
                        ret = (i, j)
                    board.removeToken(i,j)

        return ret
