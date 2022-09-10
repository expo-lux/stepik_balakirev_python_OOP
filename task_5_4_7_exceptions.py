class CellException(Exception): pass

class CellIntegerException(CellException): pass

class CellFloatException(CellException): pass

class CellStringException(CellException): pass


class CellValue:
    def __init__(self, min_value: int, max_value: int):
        self._min_value = min_value
        self._max_value = max_value

    def validate(self, value):
        raise NotImplementedError

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.validate(value)
        self.__value = value


class CellInteger(CellValue):
    def validate(self, value):
        if not self._min_value <= value <= self._max_value:
            raise CellIntegerException('значение выходит за допустимый диапазон')


class CellFloat(CellValue):
    def validate(self, value):
        if not self._min_value <= value <= self._max_value:
            raise CellFloatException('значение выходит за допустимый диапазон')


class CellString(CellValue):
    def validate(self, value):
        if not self._min_value <= len(value) <= self._max_value:
            raise CellStringException('значение выходит за допустимый диапазон')


class TupleData:
    def __init__(self, *args):
        self.__data = args

    def validate_index(self, item):
        if not 0 <= item <= len(self.__data):
            raise IndexError()

    def __getitem__(self, item):
        self.validate_index(item)
        return self.__data[item].count

    def __setitem__(self, key, value):
        self.validate_index(key)
        self.__data[key].count = value

    def __len__(self):
        return len(self.__data)

    def __iter__(self):
        for item in self.__data:
            yield item.count


ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))
x = TupleData(1, 2, 4)
for item in x:
    print(item)

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = ""
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")

t = TupleData(CellInteger(-10, 10), CellInteger(0, 2), CellString(5, 10))

d = (1, 0, 'sergey')
t[0] = d[0]
t[1] = d[1]
t[2] = d[2]
for i, x in enumerate(t):
    assert x == d[i], "объект класса TupleData хранит неверную информацию"

assert len(t) == 3, "неверное число элементов в объекте класса TupleData"

cell = CellFloat(-5, 5)
try:
    cell.value = -6.0
except CellFloatException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellFloatException"

cell = CellInteger(-1, 7)
try:
    cell.value = 8
except CellIntegerException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellIntegerException"

cell = CellString(5, 7)
try:
    cell.value = "hello world"
except CellStringException:
    assert True
else:
    assert False, "не сгенерировалось исключение CellStringException"

assert issubclass(CellIntegerException, CellException) and issubclass(CellFloatException, CellException) and issubclass(
    CellStringException,
    CellException), "классы CellIntegerException, CellFloatException, CellStringException должны наследоваться от класса CellException"
