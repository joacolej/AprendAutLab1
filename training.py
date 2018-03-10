# DEPENDENCIES ------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
import sys
import numpy as np

from main import Game
from model.features import Features
from model.values import Values
from model.player import Player

# MAIN --------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    args = len(sys.argv)
    if args == 1:
        sys.exit(0)
    op = int(sys.argv[1])
       
    iterations = 3
    f = Features()
    v = Values()
    v2 = Values()
    p = Player(v, f)
    p2 = Player(v2, f)

    for i in range (0,iterations):
        
        print("")
        print("Starting iteration number ", end="")
        print(i)
        print("")

        g = Game()
        boards = g.play(op, False, p, p2)
        board_features = []
        
        for board in boards:
            board_features.append( f.get_features(board) )

        train_values = v.assign_train_value(board_features)

        (b_function, w_function) = p.v.get_est_function()
        p2.v.set_est_function( (b_function, w_function) )

        v.update_est_function(train_values)
        
    (b_function, w_function) = p.v.get_est_function()

    fil = open("model/function", 'w')
    fil.write("\n")
    fil.write( str(b_function) )
    fil.write("\n")
    fil.write( str(w_function) )
    fil.write("\n")
    fil.close()

    