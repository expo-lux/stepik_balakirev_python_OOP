class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return True if self.is_free else False

    def __repr__(self):
        return str(self.value)


class TicTacToe:
    def __init__(self):
        self.pole = tuple(tuple(Cell() for j in range(3)) for i in range(3))
        pass

    def clear(self):
        for i in range(3):
            for j in range(3):
                self.pole[i][j].count = 0
                self.pole[i][j].is_free = True

    def check_index(self, index):
        if not 0 <= index <= 3:
            raise IndexError('неверный индекс клетки')

    def __getitem__(self, item):
        val1, val2 = item
        if isinstance(val2, slice):  # все элементы строки val1
            self.check_index(val1)
            return tuple(item.count for item in self.pole[val1])
        elif isinstance(val1, slice):  # все элементы столбца val2
            self.check_index(val2)
            return self.pole[0][val2].count, self.pole[1][val2].count, self.pole[2][val2].count
        elif isinstance(val2, int) and isinstance(val1, int):
            self.check_index(val1)
            self.check_index(val2)
            return self.pole[val1][val2].count

    def __setitem__(self, key, value):
        i, j = key
        self.check_index(i)
        self.check_index(j)
        if self.pole[i][j]:
            self.pole[i][j].is_free = False
            self.pole[i][j].count = value
        else:
            raise ValueError('клетка уже занята')


g = TicTacToe()
g.clear()
assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
g[1, 1] = 1
g[2, 1] = 2
assert g[1, 1] == 1 and g[
    2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"

try:
    res = g[3, 0]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"

try:
    g[3, 0] = 5
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"

g.clear()
g[0, 0] = 1
g[1, 0] = 2
g[2, 0] = 3

assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (
    1, 2, 3), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"

cell = Cell()
assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
res = cell.is_free
cell.is_free = True
assert bool(cell), "функция bool вернула False для свободной клетки"
