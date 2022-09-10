class Furniture:
    def __init__(self, name, weight):
        self._name, self._weight = name, weight

    def __verify_name(self, name):
        if type(name) != str:
            raise TypeError('название должно быть строкой')

    def __verify_weight(self, weight):
        if weight <= 0:
            raise TypeError('вес должен быть положительным числом')

    def __setattr__(self, key, value):
        if key == '_name':
            self.__verify_name(value)
        elif key == '_weight':
            self.__verify_weight(value)
        super().__setattr__(key, value)

    def get_attrs(self):
        t = tuple()
        for k, v in self.__dict__.items():
            if k.startswith("_") and k[1] != '_':
                t += v,
        return t


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp, self._doors = tp, doors


class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height


class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square


a = Furniture('door', 100)
cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())