class IntegerValue:

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError('возможны только целочисленные значения')
        else:
            setattr(instance, self.name, value)


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value: int = 0):
        self.value = start_value

class TableValues:
    def __init__(self, *args, **kwargs):
        self.rows, self.cols = args
        if 'cell' in kwargs:
            self.cells = tuple(tuple(kwargs['cell']() for j in range(self.cols)) for i in range(self.rows))
        else:
            raise ValueError('параметр cell не указан')

    def __getitem__(self, item):
        i, j = item
        return self.cells[i][j].count

    def __setitem__(self, key, value):
        i, j = key
        self.cells[i][j].count = value

table = TableValues(2, 3, cell=CellInteger)
print(table[0, 1])
table[1, 1] = 10
table[0, 0] = 1.45 # генерируется исключение ValueError

# вывод таблицы в консоль
for row in table.cells:
    for x in row:
        print(x.count, end=' ')
    print()
