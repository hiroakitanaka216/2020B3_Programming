import numpy as np
import math

t = np.array([-1.0, 0.0, 0.5, 2.0])


def relu(x):
    return np.maximum(0, x)


print(relu(t))
