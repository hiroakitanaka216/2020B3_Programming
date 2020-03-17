import numpy as np
from day2.task2_2 import relu
import math

x = np.array([1.0, 0.5])
W = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b = np.array([0.1, 0.2, 0.3])
#
# t = np.dot(W.T, x) + b
#
#
# def SingleLayer(tmp):
#     return np.maximum(0, tmp)
#
#
# print(SingleLayer(t))

class SingleLayer:
    def __init__(self, W, b):
        self.W = W
        self.b = b

    def forward(self, x):
        tmp = np.dot(x, self.W) + self.b
        return relu(tmp)

    def __call__(self, x):
        tmp = np.dot(x, self.W) + self.b
        return relu(tmp)

if __name__=='__main__':
    single_layer = SingleLayer(W, b)
    print(single_layer(x))



