class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.init()
        self.x = x
        self.y = y

    def init(self):
        self.x = 0
        self.y = 0

    @classmethod
    def check(cls, value):
        return type(value) in (int, float) and cls.MIN_COORD <= value <= cls.MAX_COORD

    @staticmethod
    def norm2(vector):
        return vector.x ** 2 + vector.y ** 2

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if self.check(value):
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if self.check(value):
            self.__y = value


v1 = RadiusVector2D()  # радиус-вектор с координатами (0; 0)
v2 = RadiusVector2D(1)  # радиус-вектор с координатами (1; 0)
v3 = RadiusVector2D('1', 2)
r5 = RadiusVector2D(-102, 2000)
