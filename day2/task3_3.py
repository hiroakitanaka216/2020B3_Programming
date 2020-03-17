import numpy as np

class Softmax:
    def __init__(self):
        self.out = None

    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out

        return out

    def backward(self, dout):
        dx = dout * self.out * (1 - self.out)

        return dx


aSoftmax = Softmax()
print(aSoftmax.forward(np.array([-0.5, 0.0, 1.0, 2.0])))
print(aSoftmax.backward(np.array([-0.5, 0.0, 1.0, 2.0])))
