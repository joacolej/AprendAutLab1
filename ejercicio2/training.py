# DEPENDENCIES ------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
import sys
import numpy as np
import matplotlib.pyplot as plt

from main import Game
from model.features import Features
from model.values import Values
from model.player import Player

# AUXILIAR METHODS --------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

def printIteration(i, function, learn_rate):
    (b_function, w_function) = function
    print("Starting iteration number ", end="")
    print(i)
    print("Current b_function value: ", end="")
    print(b_function)
    print("Current w_function value: ", end="")
    print(w_function)
    print("Current learn rate: ", end="")
    print(learn_rate)

def printStatistics(i, win, winc, losec, drawc):
    game_number = "Game " + str(i) + " result: "
    print(game_number, end="")
    print(win)
    print("Win count: ", end="")
    print(winc)
    print("Lose count: ", end="")
    print(losec)
    print("Draw count: ", end="")
    print(drawc)
    print("")

def printPlot(x_axis, y_axis, iterations):
    plt.plot(x_axis, y_axis, 'ro')
    plt.axis([0, iterations - 1, -2, 2])
    plt.show()

def saveFunction(op, b_function, w_function):
    filename = ""
    if op == 1:
        filename = "model/random_function"
    elif op == 2:
        filename = "model/self_function"
    else:
        filename = "model/human_function"

    fil = open(filename, 'w')
    fil.write( str(b_function) )
    fil.write("\n")
    fil.write( str(w_function) )
    fil.write("\n")
    fil.close()

# MAIN --------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # Read argument, exit if none given
    args = len(sys.argv)
    if args == 1:
        sys.exit(0)

    op = int(sys.argv[1])
    iterations = int(sys.argv[2])
    adjust_learn_rate = int(sys.argv[3])
    change_features = int(sys.argv[4])
    
    # Define main objects   
    f = Features()
    p1 = Player(Values(), f)
    p2 = Player(Values(), f)

    # Define statistics variables
    win_count = 0
    lose_count = 0
    draw_count = 0
    x_axis = []
    y_axis = []

    # Training iterations
    for i in range (0,iterations):

        if adjust_learn_rate == 1:
            p1.v.set_learn_rate( 1 - i/iterations )
        
        printIteration(i, p1.v.get_est_function(), p1.v.get_learn_rate())

        # Step 1: Create new game, p1 VS p2
        g = Game()
        boards = g.play(op, False, p1, p2)
        board_features = []

        # Step 2: Generate features for every board in the game
        for board in boards:
            board_features.append( f.get_features(board) )

        # Step 3: Using current Vop from p, estimates values for every board in the game 
        train_values = p1.v.assign_train_value(board_features)

        # Step Aux: Assign values to statistics
        (b, vtrain) = train_values[-1]
        if vtrain == 1:
            win_count = win_count + 1
        elif vtrain == -1:
            lose_count = lose_count + 1
        elif vtrain == 0:
            draw_count = draw_count + 1
        x_axis.append(i)
        y_axis.append(vtrain)
        printStatistics(i, vtrain, win_count, lose_count, draw_count)

        # Step Aux: Assign p1 current function to p2
        p2.v.set_est_function( p1.v.get_est_function() )

        # Step 4: Using LMS adjust Vop's weights
        p1.v.update_est_function(train_values)
        
    # After training finished, save result function in file   
    (b_function, w_function) = p1.v.get_est_function()
    saveFunction(op, b_function, w_function)

    printPlot(x_axis, y_axis, iterations)
    

    