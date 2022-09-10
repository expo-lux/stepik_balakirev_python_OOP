class InfFloatValue:
    @classmethod
    def validate(cls, value):
        if not type(value) in (int, float):
            raise ValueError('некорректные координаты и параметры прямоугольника')

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)


class PositiveFloatValue:
    __msg = ''

    def __init__(self, excep_msg="invalid value"):
        if not self.__class__.__msg:
            self.__class__.__msg = excep_msg

    @classmethod
    def validate(cls, value):
        if not (isinstance(value, (float, int)) and value > 0):
            raise ValueError(cls.__msg)

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)


class Rect:
    _width = PositiveFloatValue('некорректные координаты и параметры прямоугольника')
    _height = PositiveFloatValue()
    _x = InfFloatValue()
    _y = InfFloatValue()

    def __init__(self, x, y, width, height):
        self._x, self._y, self._width, self._height = x, y, width, height

    def is_collision(self, rect):
        if self._y >= rect._y - rect._height and self._y - self._height <= rect._y:
            if self._x <= rect._x + rect._width and self._x + self._width >= rect._x:
                raise TypeError('прямоугольники пересекаются')

    def __repr__(self):
        return f"_x: {self._x} _y: {self._y} _width:{self._width} _height:{self._height}"

lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]

lst_not_collision = []
for item1 in lst_rect:
    try:
        for item2 in lst_rect:
            if item1 != item2:
                item1.is_collision(item2)
    except TypeError:
        continue
    else:
        lst_not_collision.append(item1)


s1 = Rect(0,3,3,3)
s2 = Rect(2,3,1,1)
s1.is_collision(s2)
print('x')