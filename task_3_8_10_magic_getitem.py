class Cell:
    def __init__(self, value):
        self.value = value


class SparseTable:
    def __init__(self):
        self.rows, self.cols = 0, 0
        self.__data = {}
        self.__minrows, self.__mincols, self.__maxrows, self.__maxcols = 0, 0, 0, 0

    def update(self):
        temp = sorted(self.__data.keys(), key=lambda x: x[0])
        maxv = temp[-1]
        self.rows = maxv[0] + 1
        temp = sorted(self.__data.keys(), key=lambda x: x[1])
        maxv = temp[-1]
        self.cols = maxv[1] + 1

    def add_data(self, row, col, data: Cell):
        self.__data[(row, col)] = data
        self.update()

    def remove_data(self, row, col):
        if (row, col) in self.__data:
            self.__data.pop((row, col))
            self.update()
        else:
            raise IndexError('ячейка с указанными индексами не существует')

    def __getitem__(self, item):
        if item in self.__data:
            return self.__data[item].count
        else:
            raise ValueError('данные по указанным индексам отсутствуют')

    def __setitem__(self, key, value):
        row, col = key
        self.__data[key] = Cell(value)
        self.update()


st = SparseTable()
st.add_data(2, 5, Cell(25))
st.add_data(1, 1, Cell(11))
assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

try:
    v = st[3, 2]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

st[3, 2] = 100
assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"

st.remove_data(1, 1)
try:
    v = st[1, 1]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    st.remove_data(1, 1)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

d = Cell('5')
assert d.value == '5', "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"


st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
st.add_data(0, 0, Cell("cell_00"))
st[2, 5] = 25 # изменение значения существующей ячейки
st[11, 7] = 'cell_117' # создание новой ячейки
print(st[0, 0]) # cell_00
st.remove_data(2, 5)
print(st.rows, st.cols) # 12, 8 - общее число строк и столбцов в таблице
val = st[2, 5] # ValueError
st.remove_data(12, 3) # IndexError