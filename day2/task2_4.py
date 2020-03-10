import numpy as np


class MLP_3Layer:
    def __init__(self, w1, w2, w3, b1, b2, b3):
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3

    def forward(self, x):
        tmp1 = np.dot(self.w1.T, x) + self.b1
        tmp2 = np.dot(self.w2.T, tmp1) + self.b2
        tmp3 = np.dot(self.w3.T, tmp2) + self.b3
        return np.maximum(0, tmp3)


aMLP_3Layer = MLP_3Layer(np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]]), np.array([0.1, 0.4], [0.2, 0.5], [0.3, 0.6]),
                         np.array([0.1, 0.3], [0.2, 0.4]), np.array([0.1, 0.2, 0.3]), np.array([0.1, 0.2]),
                         np.array([0.1, 0.2]))
print(aMLP_3Layer.forward(np.array([[1.0, 0.5], [-0.3, -0.2], [0.0, 0.8], [0.3, -0.4]])))

#??