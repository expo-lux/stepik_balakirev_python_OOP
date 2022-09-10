from functools import total_ordering

@total_ordering
class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

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

    @property
    def volume(self):
        return self.a * self.b * self.c

    def __lt__(self, other: 'Dimensions'):
        if isinstance(other, Dimensions):
            return self.volume < other.volume

    def __eq__(self, other):
        if isinstance(other, Dimensions):
            return self.volume == other.volume

    def __repr__(self):
        return f"объем: {self.volume}"

class ShopItem:
    def __init__(self, name, price, dim: Dimensions):
        self.name = name
        self.price = price
        self.dim = dim

    def __repr__(self):
        return f"{self.name}" + " " + str(self.dim)

trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
lst_shop = (trainers, umbrella, fridge, chair)
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)
print(lst_shop_sorted)