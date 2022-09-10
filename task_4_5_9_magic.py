class PointTrack:
    def __init__(self, x, y):
        self.check_number(x)
        self.check_number(y)
        self.x, self.y = x, y

    def check_number(self, value):
        if not type(value) in (float, int):
            raise TypeError('координаты должны быть числами')

    def __repr__(self):
        return f"PointTrack: {self.x}, {self.y}"

class Track:
    def __init__(self, *args):
        self.__points = []
        if type(args[0]) in (int, float) and type(args[1]) in (int, float):
            pt = PointTrack(args[0], args[1])
            self.__points.append(pt)
        elif isinstance(args[0], PointTrack):
            for pt in args:
                self.__points.append(pt)

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points.insert(0, pt)

    def pop_back(self):
        self.__points.pop(len(self.__points) - 1)

    def pop_front(self):
        self.__points.pop(0)


tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)

