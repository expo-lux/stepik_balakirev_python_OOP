class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @classmethod
    def check_arg(cls, arg):
        return {type(arg)} <= set((int, float))

    def get_coords(self):
        return self.__x, self.__y

class Rectangle(object):
    def __init__(self, *args):
        if len(args) == 4:
            self.__sp = Point(args[0], args[1])
            self.__ep = Point(args[2], args[3])
        elif len(args) == 2:
            self.__sp = Point(*args[0].get_coords())
            self.__ep = Point(*args[1].get_coords())

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        x1, y1 = self.__sp.get_coords()
        x2, y2 = self.__ep.get_coords()
        print(f"Прямоугольник с координатами: ({x1}, {y1}) ({x2}, {y2})")

r = Rectangle(1, 2.6, 3.3, 4)
r.set_coords(Point(1, 2), Point(3, 4))
sp, ep = r.get_coords()
a, b = sp.get_coords()
c, d = ep.get_coords()
r = Rectangle(Point(1, 2), Point(3, 4))
sp, ep = r.get_coords()
a, b = sp.get_coords()
c, d = ep.get_coords()