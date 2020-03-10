import task1_1

from day2.task1_1 import Perceptron

x1_list = [1, 1, 0, 0]
x2_list = [1, 0, 1, 0]

AND = Perceptron(0.5, 0.5, 0.7)
NAND = Perceptron(-0.5, -0.5, -0.7)
OR = Perceptron(0.5, 0.5, 0)

print('AND, NAND, OR, XOR')

for i in range(0, 4):
    a = AND.forward(x1_list[i], x2_list[i])
    n = NAND.forward(x1_list[i], x2_list[i])
    o = OR.forward(x1_list[i], x2_list[i])
    x = n*o
    print(a, n, o, x)


