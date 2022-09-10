from copy import deepcopy

class Matrix:
    def __validate_index(self, indx):
        i, j = indx
        if type(j) != int or type(i) != int or j >= self.cols or i >= self.rows or i < 0 or j < 0:
            raise IndexError('недопустимые значения индексов')

    def __validate_matrix(self, lst):
        lng = len(lst[0])
        for row in lst:
            if len(row) != lng:
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            for elem in row:
                if type(elem) not in (int, float):
                    raise TypeError('список должен быть прямоугольным, состоящим из чисел')

    def __validate_values(self, rows, cols, fill_value):
        if type(rows) != int or type(rows) != int or type(fill_value) not in (int, float):
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

    def __init__(self, *args):
        if len(args) == 1:
            self.__validate_matrix(args[0])
            self.mtrx = args[0]
            self.cols = len(args[0][0])
            self.rows = len(args[0])
        else:
            rows, cols, fill_value = args
            self.__validate_values(rows, cols, fill_value)
            self.mtrx = [[fill_value for _ in range(cols)] for _ in range(rows)]
            self.cols = cols
            self.rows = rows

    def __getitem__(self, item):
        self.__validate_index(item)
        i, j = item
        return self.mtrx[i][j]

    def __setitem__(self, key, value):
        i, j = key
        self.__validate_index(key)
        if type(value) not in (int, float):
            raise TypeError('значения матрицы должны быть числами')
        self.mtrx[i][j] = value

    def __add__(self, other):
        if type(other) in (int, float):
            lst = deepcopy(self.mtrx[:])
            for i in range(self.rows):
                for j in range(self.cols):
                    lst[i][j] += other
            return Matrix(lst)
        else:
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError('операции возможны только с матрицами равных размеров')
            lst = deepcopy(other.mtrx[:])
            for i in range(self.rows):
                for j in range(self.cols):
                    lst[i][j] += self.mtrx[i][j]
            return Matrix(lst)

    def __sub__(self, other):
        if type(other) in (int, float):
            return Matrix([[self[i, j] - other for j in range(self.cols)] for i in range(self.rows)])
        else:
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError('операции возможны только с матрицами равных размеров')
            return Matrix([[self[i, j] - other[i, j] for j in range(self.cols)] for i in range(self.rows)])

    def __repr__(self):
        return "\n".join([' '.join([str(self[i, j]) for j in range(self.cols)]) for i in range(self.rows)])


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
assert m1[1, 1] == 4 and m1[0, 1] == 2 and m2[1, 1] == 1 \
       and m2[0, 0] == 1, "исходные матрицы не должны меняться при операции сложения"

m1 = Matrix(2, 2, 1)
id_m1_old = id(m1)
m2 = Matrix(2, 2, 1)
m1 = m1 + m2
id_m1_new = id(m1)
assert id_m1_old != id_m1_new, "в результате операции сложения должен создаваться НОВЫЙ экземпляр класса Matrix"

matrix = Matrix(2, 2, 0)
m = matrix + 10
assert matrix[0, 0] == matrix[1, 1] == 0, "исходные матрицa не должна меняться при операции сложения c числом"
assert m[0, 0] == 10, "неверно отработала операция сложения матрицы с числом"

m1 = Matrix(2, 2, 1)
m2 = Matrix([[0, 1], [1, 0]])
identity_matrix = m1 - m2  # должна получиться единичная матрица
assert m1[0, 0] == 1 and m1[1, 1] == 1 and m2[0, 0] == 0 \
       and m2[0, 1] == 1, "исходные матрицы не должны меняться при операции вычитания"
assert identity_matrix[0, 0] == 1 and identity_matrix[1, 1] == 1, "неверно отработала операция вычитания матриц"

matrix = Matrix(2, 2, 1)
m = matrix - 1
assert matrix[0, 0] == matrix[1, 1] == 1, "исходные матрицa не должна меняться при операции вычитания c числом"
assert m[0, 0] == m[1, 1] == 0, "неверно отработала операция вычитания числа из матрицы"
