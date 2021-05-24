import numpy as np

class vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __pos__(self):
        return self

    def __neg__(self):
        return vec2d(- self.x, - self.y)

    def __abs__(self):
        return self.mod()

    def __add__(self, other):
        if type(other) is vec2d:
            return vec2d(self.x + other.x, self.y + other.y)
        else:
            raise ValueError("Unsupported operand + for " + str(type(self)) +\
                                " and " + str(type(other)) + ".")

    def __sub__(self, other):
        if type(other) is vec2d:
            return vec2d(self.x - other.x, self.y - other.y)
        else:
            raise ValueError("Unsupported operand - for " + str(type(self)) +\
                                " and " + str(type(other)) + ".")

    def __mul__(self, other):
        if type(other) is vec2d:
            return self.x * other.x + self.y * other.y
        else:
            return vec2d(self.x * other, self.y * other)

    def __rmul__(self, other):
        if type(other) is vec2d:
            return self.x * other.x + self.y * other.y
        else:
            return vec2d(self.x * other, self.y * other)

    def __truediv__(self, scalar):
        return vec2d(self.x / scalar, self.y / scalar)

    def __pow__(self, power):
        return self.mod()**power

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __mod__(self, other):
        return vec2d(self.x % other, self.y % other)

    def mod(self):
        return np.sqrt(self.x**2 + self.y**2)

    def unit(self):
        return vec2d(self.x, self.y) / self.mod()

    def get_angle(self, other):
        if type(other) is vec2d:
            return np.arccos(self * other / (self.mod() * other.mod()))
        else:
            raise ValueError("Unsupported operation for " + str(type(self)) +\
                                " and " + str(type(other)) + ".")
