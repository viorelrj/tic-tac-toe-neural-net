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
    pbar = Bar("Learning ...", max = iterations)
    for i in range(0, iterations):
        board = np.random.randint(0, 3, 9)
        instance.learn(board)
        pbar.next()
    np.save(output +".npy", instance.weights)
    pbar.finish()


weights = load_weights('weights_rules')
greg = Intelligence(weights, .0005)
teach(greg, 'weights_rules', 100000)

