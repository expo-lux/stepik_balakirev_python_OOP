class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    @classmethod
    def check_type(cls, value):
        if not type(value) in [int, float]:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __setattr__(self, key, value):
        if key == 'radius':
            if value > 0:
                super().__setattr__(key, value)
        else:
            super().__setattr__(key, value)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.check_type(value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.check_type(value)
        self.__y = value

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.check_type(value)
        self.__radius = value

    def __getattr__(self, item):
        return False

circle = Circle(1, 7, 22)
print(circle.__dict__)
print(Circle.__dict__)
circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
x, y = circle.x, circle.y
res = circle.name