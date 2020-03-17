import numpy as np
class relu:
    def __init__(self):
        self.mask = None

    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0
        
        return out

    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout

        return dx

arelu = relu()
out = arelu.forward(np.array([-0.5, 0.0, 1.0, 2.0]))
print(out)

dout = np.zeros_like(out)

for i in range(len(out)):
    if out[i] != 0:
        dout[i] = 1

dx = arelu.backward(dout)
print(dx)

