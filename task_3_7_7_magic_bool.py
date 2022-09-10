class Ellipse:
    def __init__(self, *args):
        if len(args) == 4:
            self.x1, self.y1, self.x2, self.y2 = args
        elif len(args) == 0:
            pass
        else:
            raise ValueError("invalid")

    def __bool__(self):
        return hasattr(self, 'x1') and \
               hasattr(self, 'x2') and \
               hasattr(self, 'y1') and \
               hasattr(self, 'y2')

    def get_coords(self):
        if self:
            return self.x1, self.y1, self.x2, self.y2
        else:
            raise AttributeError('нет координат для извлечения')

lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]
for item in lst_geom:
    if item:
        item.get_coords()