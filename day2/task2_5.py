import numpy as np

# a = np.array([0.3, 0.9, 4.0])

def softmax(x):
    exp_x = np.exp(x)
    sum_exp_x = np.sum(exp_x)
    return exp_x / sum_exp_x

print(softmax(a))
