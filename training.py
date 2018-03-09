# DEPENDENCIES ------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
import sys
import numpy as np

from main import Game
from model.features import Features
from model.values import Values
from model.player import Player

# AUXILIAR METHODS --------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

# MAIN --------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    args = len(sys.argv)
    if args == 1:
        sys.exit(0)
    op = int(sys.argv[1])
       
    iterations = 20
    f = Features()
    v = Values()
    p = Player(v, f)

    for i in range (0,iterations):
        
        print("")
        print("Starting iteration number ", end="")
        print(i)
        print("")

        g = Game()
        boards = g.play(op, False, p)
        board_features = []
        print("1 - Game finished")
        
        for board in boards:
            board_features.append( f.get_features(board) )
        print("2 - Features extracted")

        train_values = v.assign_train_value(board_features)
        print("3 - Train pairs generated")

        v.update_est_function(train_values)
        print("4 - Function updated")

        (b_function, w_function) = p.v.get_est_function()
        print(str((b_function, w_function)))

        fil = open("model/function", 'w')
        fil.write("\n")
        fil.write( str(b_function) )
        fil.write( str(w_function) )
        fil.write("\n")
        fil.close()

    