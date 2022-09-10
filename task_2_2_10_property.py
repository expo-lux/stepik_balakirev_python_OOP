class LineTo:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        """Строковое представление - для отладки"""
        return f"R {self.x}:{self.y}"

    def __str__(self):
        """Строковое представление - для отладки"""
        return f"{self.x}:{self.y}"


class PathLines:
    def __init__(self, *args):
        # добавляем одну линию из начала координат
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


p = PathLines(LineTo(0, 0), LineTo(1, 0))
for i in range(2, 11):
    p.add_line(LineTo(i))

print(p.get_path())
print(list(map(print, p.get_path())))
# print(p.get_length())
