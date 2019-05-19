# This is the sequential algorithm for neural network




# This is the neural netowrk ai for tic tac toe.
# Input array consists of 27 elements: 3 per each cell of board, with each one described as follows:
# 1st - cell is free, 2nd cell is occupied by the ai,  3rd - cell is occupied by oponent
# 
# There is only one hidden layer, with 10 elements, each representing a move: 9 cells and 10th - no move available.
# 
# The output layer consists of one element which contains one cell - the index of cell with biggest value from hidden layer.





import numpy as np





####################
# Will be Imported #
####################

# Generate inital weights, 27 for each of nine hidden layers
weights = np.random.rand(10, 27)


for epoch in range(0, 50000):

    # The imported board will look as an array of integer values 0, 1, 2, representing the state.
    # Currently, generating a random table, to teach the net to make a move to an empty cell.
    board = np.random.randint(0, 3, 9)






    ##################
    # Neural Network #
    ##################
    learning_rate = 0.7

    def sigmoid(x):  
        return 1/(1+np.exp(-x))

    def sigmoid_der(x):  
        return sigmoid(x)*(1-sigmoid(x))



    # Convert board state into neural network input layer model, described in the header of the file
    input_layer = np.zeros(27)
    for cell, state in enumerate(board):
        input_layer[cell * 3 + state] = 1

    # Hidden layer
    hidden_layer = np.zeros(10)
    for i in range(0, len(hidden_layer)):
        hidden_layer[i] = sigmoid(np.dot(input_layer, weights[i]))


    choice = np.argmax(hidden_layer)



    ####################
    # Back propagation #
    ####################

    answer = board
    answer[answer != 0] = 1
    answer = np.abs(1 - answer)
    if (np.count_nonzero(answer) == 9):
        no_choice = 1
    else:
        no_choice = 0
    answer = np.append(answer, no_choice)


    error = hidden_layer - answer
    print(error.sum())

    for i in range(0, 10):
        # backpropagation step 2
        dcost_dpred = error[i]
        dpred_dz = sigmoid_der(hidden_layer[i])

        z_delta = dcost_dpred * dpred_dz
        weights[i] -= learning_rate * np.dot(input_layer, z_delta)
        