class PositiveFloatValue:
    __msg = ''

    def __init__(self, excep_msg="invalid value"):
        if not self.__class__.__msg:
            self.__class__.__msg = excep_msg

    @classmethod
    def validate(cls, value):
        if not (isinstance(value, (float, int)) and value > 0):
            raise ValueError(cls.__msg)

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)


class Triangle:
    a = PositiveFloatValue("длины сторон треугольника должны быть положительными числами")
    b = PositiveFloatValue()
    c = PositiveFloatValue()

    def __init__(self, a, b, c):
        self.a = a  # валидация типа и значения
        self.b = b
        self.c = c
        if not (a < b + c and b < a + c and c < a + b):  #
            raise ValueError("с указанными длинами нельзя образовать треугольник")

    def __len__(self):
        return int(self.a + self.b + self.c)

    def __call__(self):
        p = len(self)/2
        return pow(p * (p - self.a) * (p - self.b) * (p - self.c), 0.5)


tr = Triangle(5, 4, 3)
assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"

try:
    tr = Triangle(-5, 4, 3)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    tr = Triangle(10, 1, 1)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

tr = Triangle(5, 4, 3)
assert len(tr) == 12, "функция len вернула неверное значение"
assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"