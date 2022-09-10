class Digit:
    def __init__(self, value):
        if not type(value) in (int, float):
            raise TypeError('значение не соответствует типу объекта')
        self.value = value

class Integer(Digit):
    def __init__(self, value):
        if type(value) != int:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)

class Float(Digit):
    def __init__(self, value):
        if type(value) != float:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)

class Positive(Digit):
    def __init__(self, value):
        if not value > 0:
            raise TypeError(f'{value}значение не соответствует типу объекта')
        super().__init__(value)

class Negative(Digit):
    def __init__(self, value):
        if not value < 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)

class PrimeNumber(Integer, Positive):
    def __init__(self, value):
        super().__init__(value)

class FloatPositive(Float, Positive):
    def __init__(self, value):
        super().__init__(value)


digits = [PrimeNumber(i) for i in range(1, 4)]
digits += [FloatPositive(float(i)) for i in range(1, 6)]
lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))
print('a')
