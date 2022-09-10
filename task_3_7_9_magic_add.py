class Vector:
    def __init__(self, *args):
        self.coords = list(args)

    def check(self, other):
        if len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')

    def __add__(self, other: 'Vector'):
        self.check(other)
        return Vector(*list(other.coords[i] + self.coords[i] for i in range(len(self.coords))))

    def __sub__(self, other):
        self.check(other)
        return Vector(*list(self.coords[i] - other.coords[i] for i in range(len(self.coords))))

    def __mul__(self, other):
        self.check(other)
        return Vector(*list(self.coords[i] * other.coords[i] for i in range(len(self.coords))))

    def __iadd__(self, other: float):
        if isinstance(other, (int, float)):
            for i, v in enumerate(self.coords):
                self.coords[i] += other
        elif isinstance(other, Vector):
            self.check(other)
            for i, v in enumerate(self.coords):
                self.coords[i] += other.coords[i]
        return self

    def __isub__(self, other: float):
        if isinstance(other, (int, float)):
            for i, v in enumerate(self.coords):
                self.coords[i] -= other
        elif isinstance(other, Vector):
            self.check(other)
            for i, v in enumerate(self.coords):
                self.coords[i] -= other.coords[i]
        return self

    def __eq__(self, other):
        self.check(other)
        return all(other.coords[i] == self.coords[i] for i, v in enumerate(self.coords))

    def __ne__(self, other):
        self.check(other)
        return any(other.coords[i] != self.coords[i] for i, v in enumerate(self.coords))

    def __repr__(self):
        return ":".join(str(item) for item in self.coords)


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).coords)  # [5, 7, 9]
print((v1 - v2).coords)  # [-3, -3, -3]
print((v1 * v2).coords)  # [4, 10, 18]

v1 += 10
print(v1.coords)  # [11, 12, 13]
v1 -= 10
print(v1.coords)  # [1, 2, 3]
v1 += v2
print(v1.coords)  # [5, 7, 9]
v2 -= v1
print(v2.coords)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True