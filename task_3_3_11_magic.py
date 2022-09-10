class PolyLine:
    def __init__(self, *args):
        self.__l = list(args)

    def add_coord(self, x, y):
        self.__l.append((x,y))

    def remove_coord(self, indx):
        self.__l.pop(indx)

    def get_coords(self):
        return self.__l

poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
poly.add_coord(1,1)
print(poly.get_coords())