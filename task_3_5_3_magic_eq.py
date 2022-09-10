# код из задачи 2.2.9
class LineTo:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        """Строковое представление - для отладки"""
        return f"{self.x}:{self.y}"


class PathLines:
    def __init__(self, *args):
        # добавляем одну линию(точку) из начала координат
        self.__lines = [LineTo()] + list(args)

    @staticmethod
    def distance(a: LineTo, b: LineTo):
        """Возвращает расстрояние между двумя точками"""
        return pow((b.x - a.x) ** 2 + (b.y - a.y) ** 2, 0.5)

    def get_length(self):
        return sum(map(self.distance, self.__lines, self.get_path()))

    def get_path(self) -> list:
        return self.__lines[1:]

    def add_line(self, line):
        self.__lines.append(line)


# код для классов-наследников из задачи 3.5.3
class TrackLine(LineTo):  # наследуемся от класса LineTo
    def __init__(self, to_x: float, to_y: float, max_speed: int):
        self.to_x, self.to_y, self.max_speed = to_x, to_y, max_speed
        super().__init__(to_x, to_y)  # вызываем конструктор(инициализатор) класса LineTo


class Track(PathLines): #наследуемся от PathLines
    def __init__(self, start_x, start_y):
        # вызываем конструктор PathLines, передавая начало маршрута как первый сегмент
        super().__init__(TrackLine(start_x, start_y, 60))
        #PathLines считает длину маршрута от начала координат - а нам надо от (start_x, start_y)
        #так что длину первого сегмента сохраняем, затем ее вычтем из суммарной длины
        self.__firstlen = self.get_length()

    def add_track(self, tr: TrackLine):
        self.add_line(tr)

    def get_tracks(self):
        # PathLines.get_path() выдает список -> переводим его кортеж, как требуется по ТЗ
        return tuple(self.get_path())

    def __len__(self):
        return int(self.get_length() - self.__firstlen) #отнимаем длину первого сегмента

    @staticmethod
    def check_type(obj):
        if not isinstance(obj, Track):
            raise TypeError(f"Incorrect operand type: {type(obj)} instead Track")

    def __eq__(self, other):
        self.check_type(other)
        return len(self) == len(other)

    def __lt__(self, other):
        self.check_type(other)
        return len(self) < len(other)


track1, track2 = Track(0, 0), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2

