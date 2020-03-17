class Multiply:
    def __init__(self):
        """	逆伝播計算に必要な変数：forwardの入力値	"""
        self.x = None
        self.y = None
    def forward(self, x, y):
        """	順伝播計算：z	=	x	*	y	"""
        self.x = x
        self.y = y
        z = x * y
        return z
    def	backprop(self, dz):
        """	逆伝播計算:	dz/dx	=	y,	dz/dy	=	x	"""
        dx = dz * self.y
        dy = dz * self.x
        return dx, dy

class Add:
    def __init__(self):
        self.x = None
        self.y = None
    def forward(self, x, y):
        self.x = x
        self.y = y
        z = x + y
        return z
    def backprop(self, dz):
        dx = dz
        dy = dz
        return dx, dy

a = 2
b = 3
c = 4

aAdd = Add()
aMultiply = Multiply()
aplusb = aAdd.forward(a, b)
y = aMultiply.forward(aplusb, c)
print(y)

dc = y/c
print(aAdd.backprop(y/dc), dc)

