from copy import deepcopy


class Matrix:
    def __init__(self, *args):
        if len(args) == 1:  # 2d список
            self.check_list(args[0])
            self.__data = deepcopy(args[0])
            self.__rows, self.__cols = len(args[0]), len(args[0][0])
        elif len(args) == 3:  # rows, cols, fill_value
            rows, cols, fill_value = args
            self.check_args(rows, cols, fill_value)
            self.__data = [[fill_value for j in range(cols)] for i in range(rows)]
            self.__rows, self.__cols = rows, cols

    @property
    def rows(self):
        return self.__rows

    @property
    def cols(self):
        return self.__cols

    @staticmethod
    def list2tuple(lst: list) -> tuple:
        return tuple(tuple(col for col in row)
                     for row in lst)

    @staticmethod
    def check_args(rows, cols, fill_value):
        if not (type(rows) == int and type(cols) == int
                and type(fill_value) in (int, float)):
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

    @staticmethod
    def check_list(lst: list):
        """Валидация - 2D список прямоугольной формы? все элементы в нем - числа?"""
        cols = len(lst[0])
        is_rectangular = all(map(lambda x: x == cols, [len(row) for row in lst]))
        is_valid = all(map(lambda x: type(x) in (int, float), [item for row in lst for item in row]))
        if not (is_rectangular and is_valid):
            raise TypeError('список должен быть прямоугольным, состоящим из чисел')

    def check_index(self, indexes: tuple):
        row, col = indexes
        if not (type(row) == int and type(col) == int and
                0 <= row < len(self.__data) and
                0 <= col < len(self.__data[0])):
            raise IndexError('недопустимые значения индексов')

    @staticmethod
    def check_value(value):
        if not type(value) in (int, float):
            raise TypeError('значения матрицы должны быть числами')

    def is_valid_operand(self, obj: 'Matrix'):
        if not (obj.rows == self.rows and obj.cols == self.cols):
            raise ValueError('операции возможны только с матрицами равных размеров')

    def __getitem__(self, item):
        self.check_index(item)
        row, col = item
        return self.__data[row][col]

    def __setitem__(self, key, value):
        self.check_index(key)
        self.check_value(value)
        row, col = key
        self.__data[row][col] = value

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[col + other for col in row] for row in self.__data])
        elif isinstance(other, Matrix):
            self.is_valid_operand(other)
            return Matrix([[self[i, j] + other[i, j] for j in range(self.cols)] for i in range(self.rows)])

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[col - other for col in row] for row in self.__data])
        elif isinstance(other, Matrix):
            self.is_valid_operand(other)
            return Matrix([[self[i, j] - other[i, j] for j in range(self.cols)] for i in range(self.rows)])


list2D = [[1, 2], [3, 4], [5, 6, 7]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не прямоугольного списка в конструкторе Matrix"

list2D = [[1, []], [3, 4], [5, 6]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для списка не из чисел в конструкторе Matrix"

try:
    st = Matrix('1', 2, 0)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не числовых аргументов в конструкторе Matrix"

list2D = [[1, 2], [3, 4], [5, 6]]
matrix = Matrix(list2D)
assert matrix[2, 1] == 6, "неверно отработал конструктор или __getitem__"

matrix = Matrix(4, 5, 10)
assert matrix[3, 4] == 10, "неверно отработал конструктор или __getitem__"

try:
    v = matrix[3, -1]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

try:
    v = matrix['0', 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

matrix[0, 0] = 7
assert matrix[0, 0] == 7, "неверно отработал __setitem__"

try:
    matrix[0, 0] = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError в __setitem__"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1], [1, 1]])

try:
    matrix = m1 + m2
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при сложении матриц разных размеров"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1]])
matrix = m1 + m2
assert isinstance(matrix, Matrix), "операция сложения матриц должна возвращать экземпляр класса Matrix"
assert matrix[1, 1] == 5, "неверно отработала операция сложения матриц"
assert m1[1, 1] == 4 or m2[1, 1] == 1, "исходные матрицы не должны меняться при операции сложения"

m1 = Matrix(2, 2, 1)
id_m1_old = id(m1)
m2 = Matrix(2, 2, 1)
m1 = m1 + m2
id_m1_new = id(m1)
assert id_m1_old != id_m1_new, "в результате операции сложения должен создаваться НОВЫЙ экземпляр класса Matrix"

matrix = Matrix(2, 2, 0)
matrix = matrix + 10
assert matrix[0, 0] == 10, "неверно отработала операция сложения матрицы с числом"

m1 = Matrix(2, 2, 1)
m2 = Matrix([[0, 1], [1, 0]])
identity_matrix = m1 - m2  # должна получиться единичная матрица
assert identity_matrix[0, 0] == 1 and identity_matrix[1, 1] == 1, "неверно отработала операция вычитания матриц"

matrix = Matrix(2, 2, 1)
matrix = matrix - 1
assert matrix[1, 1] == 0, "неверно отработала операция вычитания числа из матрицы"
