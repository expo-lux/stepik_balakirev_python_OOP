class Vector:
    def __init__(self, *args):
        self.coords = list(args)

    def check(self, other):
        if len(self.coords) != len(other.coords):
            raise TypeError('размерности векторов не совпадают')

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

    def get_coords(self):
        return tuple(self.coords)


class VectorInt(Vector):
    def __init__(self, *args):
        for item in args:
            if type(item) != int:
                raise ValueError('координаты должны быть целыми числами')
        super().__init__(*args)

    def __add__(self, other):
        self.check(other)
        if any(map(lambda item: type(item) == float, other.get_coords())):
            return super().__add__(other)
        else:
            return VectorInt(*(other.coords[i] + self.coords[i] for i in range(len(self.coords))))

    def __sub__(self, other):
        self.check(other)
        if any(map(lambda item: type(item) == float, other.get_coords())):
            return super().__sub__(other)
        else:
            return VectorInt(*(self.coords[i] - other.coords[i] for i in range(len(self.coords))))


v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)

assert (v1 + v2).get_coords() == (
4, 6, 8), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
assert (v1 - v2).get_coords() == (
-2, -2, -2), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"

v = VectorInt(1, 2, 3, 4)
assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"

try:
    v = VectorInt(1, 2, 3.4, 4)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"

v1 = VectorInt(1, 2, 3, 4)
v2 = VectorInt(4, 2, 3, 4)
v3 = Vector(1.0, 2, 3, 4)

v = v1 + v2
assert type(
    v) == VectorInt, "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
v = v1 + v3
assert type(v) == Vector, "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"