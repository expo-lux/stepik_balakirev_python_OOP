class ListMath:
    def __init__(self, lst=None):
        if lst:
            self.__l = list(filter(lambda x: type(x) in (int, float), lst))
        else:
            self.__l = []
        self.lst_math = self.__l

    @staticmethod
    def check_type(value):
        if type(value) not in (int, float):
            raise TypeError("Invalid type")

    def __str__(self):
        return str(self.__l)

    def __add__(self, other):
        self.check_type(other)
        return ListMath([item + other for item in self.__l])

    def __radd__(self, other):
        self.check_type(other)
        return self + other

    def __iadd__(self, other):
        self.check_type(other)
        return self + other

    def __sub__(self, other):
        self.check_type(other)
        return ListMath([item - other for item in self.__l])

    def __rsub__(self, other):
        self.check_type(other)
        return ListMath([other - item for item in self.__l])

    def __mul__(self, other):
        self.check_type(other)
        return ListMath([item * other for item in self.__l])

    def __rmul__(self, other):
        self.check_type(other)
        return self * other

    def __truediv__(self, other):
        self.check_type(other)
        return ListMath([item / other for item in self.__l])

    def __rtruediv__(self, other):
        self.check_type(other)
        return ListMath([other / item for item in self.__l])



lst1 = ListMath()
lp = [1, False, 2, -5, "abc", 7]
lst2 = ListMath(lp)
lst3 = ListMath(lp)

assert id(lst2.lst_math) != id(lst3.lst_math), "внутри объектов класса ListMath должна создаваться копия списка"