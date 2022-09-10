from math import floor as fl


class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size
        self.m = []

    def check_matrix(self):
        """Валидация - матрица прямоугольной формы? все элементы в ней - числа?"""
        cols = len(self.m[0])
        is_rectangular = all(map(lambda x: x == cols, [len(row) for row in self.m]))
        is_valid = all(map(lambda x: type(x) in (int, float), [item for row in self.m for item in row]))
        if not (is_rectangular and is_valid):
            raise ValueError("Неверный формат для первого параметра matrix.")

    def slice_and_flatten(self, i, j):
        """Вырезает матрицу размером self.size[0] x self.size[1] и возвращает ее в виде списка"""
        """i, j - координаты левого верхнего угла вырезаемой матрицы"""
        return [item
                for row in self.m[i:i + self.size[1]]
                for item in row[j:j + self.size[0]]]

    @staticmethod
    def pretty_print2D(temp: list):
        """Распечатка матрицы"""
        for row in temp:
            print()
            for item in row:
                print(item, end='\t\t')
        print()

    def __call__(self, m: list):
        """Возвращает матрицу с максимальными значениями в соответствии с ТЗ"""
        self.m = m
        self.check_matrix()
        rows = len(m) // self.step[1]
        cols = len(m[0]) // self.step[0]
        res = [[0] * cols for i in range(rows)]
        stopI = fl(len(m) / self.step[1]) * self.step[1]
        stopJ = fl(len(m[0]) / self.step[0]) * self.step[0]
        for i in range(0, stopI, self.step[1]):
            for j in range(0, stopJ, self.step[0]):
                row = int(i / self.step[1])
                col = int(j / self.step[0])
                res[row][col] = max(self.slice_and_flatten(i, j))
        return res


mp = MaxPooling(step=(2, 2), size=(2,2))
m1 = [[1, 10, 10], [5, 10, 0], [0, 1, 2]]
m2 = [[1, 10, 10, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res1 = mp(m1)
res2 = mp(m2)

assert res1 == [[10]], "неверный результат операции MaxPooling"
assert res2 == [[10, 12], [40, 300]], "неверный результат операции MaxPooling"

mp = MaxPooling(step=(3, 3), size=(2,2))
m3 = [[1, 12, 14, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res3 = mp(m3)
assert res3 == [[12]], "неверный результат операции при MaxPooling(step=(3, 3), size=(2,2))"

try:
    res = mp([[1, 2], [3, 4, 5]])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не прямоугольную матрицу"

try:
    res = mp([[1, 2], [3, '4']])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не числовые значения в матрице"