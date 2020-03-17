import numpy as np
from day2.task2_3 import SingleLayer


class MLP_3Layer:
    def __init__(self, w1, w2, w3, b1, b2, b3):
        self.single_layer1 = SingleLayer(w1, b1)
        self.single_layer2 = SingleLayer(w2, b2)
        self.single_layer3 = SingleLayer(w3, b3)

    def forward(self, x):
        tmp1 = self.single_layer1.forward(x)
        tmp2 = self.single_layer2.forward(tmp1)
        tmp3 = self.single_layer3.forward(tmp2)
        return tmp3


aMLP_3Layer = MLP_3Layer(np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]]),
                         np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]]),
                         np.array([[0.1, 0.3], [0.2, 0.4]]),
                         np.array([0.1, 0.2, 0.3]),
                         np.array([0.1, 0.2]),
                         np.array([0.1, 0.2]))
print(aMLP_3Layer.forward(np.array([[1.0, 0.5], [-0.3, -0.2], [0.0, 0.8], [0.3, -0.4]])))
