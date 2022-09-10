class Track:
    def __init__(self, start_x, start_y):
        self.__segments = []

    def add_point(self, x, y, speed):
        self.__segments.append([(x, y), speed])

    def __getitem__(self, item):
        self.check_index(item)
        return self.__segments[item]

    def __setitem__(self, key, value):
        self.check_index(key)
        self.__segments[key][1] = value

    def check_index(self, index):
        if index < 0 or index >= len(self.__segments):
            raise IndexError('некорректный индекс')


tr = Track(10, -5.4)
tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)

res = tr[3]  # IndexError
