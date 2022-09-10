class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c):
        self.init()
        self.a = a
        self.b = b
        self.c = c

    def init(self):
        self.a, self.b, self.c = 0, 0, 0

    @classmethod
    def check(cls, value):
        return cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION

    def __setattr__(self, key, value):
        if key in ['MIN_DIMENSION', 'MAX_DIMENSION']:
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        else:
            super().__setattr__(key, value)

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.check(value):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.check(value):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.check(value):
            self.__c = value


d = Dimensions(10.5, 20.1, 30)
d.a = 8
d.b = 15
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
d.MAX_DIMENSION = 10  # исключение AttributeError
