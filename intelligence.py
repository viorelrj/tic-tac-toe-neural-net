# This is the neural netowrk ai for tic tac toe.
# Input array consists of 27 elements: 3 per each cell of board, with each one described as follows:
# 1st - cell is free, 2nd cell is occupied by the ai,  3rd - cell is occupied by oponent
# 
# There is only one hidden layer, with 10 elements, each representing a move: 9 cells and 10th - no move available.
# 
# The output layer consists of one element which contains one cell - the index of cell with biggest value from hidden layer.

import numpy as np

class Intelligence:
    def __init__(self, weights, learning_rate):
        self.weights = weights
        self.learning_rate = learning_rate
        self.choice = None
        self.error = None


    def sigmoid(self, x):  
        return 1/(1+np.exp(-x))


    def sigmoid_der(self, x):  
        return self.sigmoid(x)*(1-self.sigmoid(x))


    def step(self, board):
        # Convert board state into neural network input layer model, described in the header of the file
        input_layer = np.zeros(27)
        for cell, state in enumerate(board):
            input_layer[np.int(cell * 3 + state)] = 1

        hidden_layer = np.zeros(10)
        for i in range(0, len(hidden_layer)):
            hidden_layer[i] = self.sigmoid(np.dot(input_layer, self.weights[i]))

        return np.argmax(hidden_layer)



    def learn(self, board):
        # Convert board state into neural network input layer model, described in the header of the file
        input_layer = np.zeros(27)
        for cell, state in enumerate(board):
            input_layer[cell * 3 + state] = 1

        # Feed Forward
        hidden_layer = np.zeros(10)
        for i in range(0, len(hidden_layer)):
            hidden_layer[i] = self.sigmoid(np.dot(input_layer, self.weights[i]))

        self.choice = np.argmax(hidden_layer)

        # Back propagation
        answer = board
        answer[answer != 0] = 1
        answer = np.abs(1 - answer)
        if (np.count_nonzero(answer) == 9):
            no_choice = 1
        else:
            no_choice = 0
        answer = np.append(answer, no_choice)

        self.error = hidden_layer - answer

        for i in range(0, 10):
            # backpropagation step 2
            dcost_dpred = self.error[i]
            dpred_dz = self.sigmoid_der(hidden_layer[i])

            z_delta = dcost_dpred * dpred_dz
            self.weights[i] -= self.learning_rate * np.dot(input_layer, z_delta)
        
        return self.choice
            



