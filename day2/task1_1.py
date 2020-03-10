class Perceptron:
    def __init__(self, w1, w2, theta):
        self.w1 = 0
        self.w2 = 0
        self.theta = 0

    def forward(self, x1, x2):
        tmp = self.w1 * x1 + self.w2 * x2
        return 0 if tmp <= self.theta else 1
        # if tmp <= self.theta:
        #     y=0
        # else:
        #     y=1
        # return y
