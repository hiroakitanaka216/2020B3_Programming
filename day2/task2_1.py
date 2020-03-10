import numpy as np
import math

t = np.array([-1.0, 0.0, 0.5, 2.0])


def sigmoid(x):
    return 1 / (1 + math.e ** -x)


print(sigmoid(t))
