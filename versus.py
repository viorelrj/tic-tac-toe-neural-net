import os
import numpy as np
from progress.bar import Bar
from intelligence import Intelligence

def load_weights(name):
    exists = os.path.isfile(name + '.npy')
    if (exists):
        weights = np.load(name +'.npy')
    else:
        weights = np.random.rand(10, 27)
    return weights

def teach(instance, output, iterations):
    pbar = Bar("The neural net is learning ...", max = iterations)
    for i in range(0, iterations):
        board = np.random.randint(0, 3, 9)
        instance.learn(board)
        pbar.next()
    np.save(output +".npy", instance.weights)
    pbar.finish()

def checkWin(board):
    for i in range(0, 3):
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] and board[i * 3] != 0:
            return board[i * 3]
        if board[i] == board[i + 3] == board[i + 6] and board[i] != 0:
            return board[i]

    if board[0] == board[4] == board[8] and board[0] != 0:
        return board[0]
    if board[2] == board[4] == board[6] and board[2] != 0:
        return board[2]
    
    if not 0 in board:
        return 0
    else:
        return None

X = Intelligence(load_weights('weights_X'), 0.05)
O = Intelligence(load_weights('weights_O'), 0.05)

board = np.zeros(9)
board[bob.step(board)] = ''
