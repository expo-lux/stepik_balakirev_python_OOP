class FloatValue:
    @classmethod
    def validate(cls, value):
        if not isinstance(value, float):
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        print(f"\n__get__ called on FloatValue. Instance is {instance}. Class type is {owner}")
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, value):
        self.value = value


class TableSheet:

    def __init__(self, N, M):
        self.cells = [[Cell(0.0) for col in range(M)] for row in range(N)]


x = Cell(1.0)

rows, cols = 5, 3
table = TableSheet(rows, cols)
for row in range(1, rows + 1):
    print('')
    for col in range(1, cols + 1):
        value = float(col + 3 * (row - 1))
        table.cells[row - 1][col - 1].value = value
        print(table.cells[row - 1][col - 1].value, end=' ')
