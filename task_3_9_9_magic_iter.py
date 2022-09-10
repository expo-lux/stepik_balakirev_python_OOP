class Cell:
    def __init__(self, data):
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    def __repr__(self):
        return str(f"Cell id {id(self)}, value {self.data}")


class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.__data = tuple(tuple(Cell(0) for j in range(cols)) for i in range(rows))
        self.__rows, self.__cols = rows, cols
        self.__type = type_data

    def check_index(self, indexes: tuple):
        row, col = indexes
        if not (type(row) == int and type(col) == int and
                0 <= row <= self.__rows and
                0 <= col <= self.__cols):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.check_index(item)
        row, col = item
        return self.__data[row][col].data

    def __setitem__(self, key, value):
        self.check_index(key)
        if type(value) != self.__type:
            raise TypeError('неверный тип присваиваемых данных')
        row, col = key
        self.__data[row][col].data = value

    def __iter__(self):
        self.__iter_row = -1
        return self

    def __next__(self):
        if self.__iter_row == self.__rows - 1:
            raise StopIteration
        else:
            self.__iter_row += 1
            return iter(item.data for item in self.__data[self.__iter_row])


tb = TableValues(3, 2)
n = m = 0
for row in tb:
    n += 1
    for value in row:
        m += 1
        print(type(value), value)
        assert type(
            value) == int and value == 0, "при переборе объекта класса TableValues с помощью вложенных циклов for, должен сначала возвращаться итератор для строк, а затем, этот итератор должен возвращать целые числа (значения соответствующих ячеек)"

assert n > 1 and m > 1, "неверно отработали вложенные циклы для перебора ячеек таблицы"

tb[0, 0] = 10
assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"

try:
    tb[2, 0] = 5.2
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"
