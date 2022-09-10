class ItemAttrs:
    def __init__(self):
        pass

    def __getitem__(self, indx):
        for i, v in enumerate(self.__dict__.values()):
            if i == indx:
                return v

    def __setitem__(self, indx, value):
        i = 0
        for item in self.__dict__:
            if indx == i:
                self.__dict__[item] = value
                break
            i += 1


class Point(ItemAttrs):
    def __init__(self, x, y):
        self.x, self.y = x, y

pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]   # 2.5
pt[0] = 10