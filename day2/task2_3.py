import numpy as np
import math

x = np.array([1.0, 0.5])
W = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b = np.array([0.1, 0.2, 0.3])

t = np.dot(W.T, x) + b


def SingleLayer(tmp):
    return np.maximum(0, tmp)


print(SingleLayer(t))
