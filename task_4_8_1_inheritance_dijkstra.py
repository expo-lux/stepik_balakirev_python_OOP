from math import inf


class Vertex:
    def __init__(self):
        self._links = []

    @property
    def links(self):
        return self._links


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return self.name


class Link:
    def __init__(self, v1: 'Vertex', v2: 'Vertex'):
        self._v1, self._v2, self.dist = v1, v2, 1
        self._v1.links.append(self)
        self._v2.links.append(self)

    def __eq__(self, other):
        if isinstance(other, Link):
            return self.v1 == other.v1 and self.v2 == other.v2 or \
                   self.v1 == other.v2 and self.v2 == other.v1
        elif isinstance(other, tuple):
            return self.v1 == other[0] and self.v2 == other[1] or \
                   self.v1 == other[1] and self.v2 == other[0]
        else:
            raise TypeError("Link: invalid type")

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value):
        if type(value) in (int, float) and value > 0:
            self._dist = value


class LinkMetro(Link):
    def __init__(self, v1: Station, v2: Station, dist: float):
        super().__init__(v1, v2)
        self.dist = dist

    def __repr__(self):
        return f"{self.v1.name} {self.v2.name} {self.dist}"


class LinkedGraph:
    def __init__(self):
        self._links, self._vertex = [], []

    def add_vertex(self, value: Vertex):
        """добавлениe новой вершины v в список _vertex (если она там отсутствует)"""
        if value not in self._vertex:
            self._vertex.append(value)

    def add_link(self, link: Link):
        """добавлениe новой связи link в список _links (если объект link с указанными вершинами в списке отсутствует)"""
        if link not in self._links:
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)

    def get_link(self, vertex1: Vertex, vertex2: Vertex):
        """поиск линка по вершинам"""
        for link in vertex1.links:
            if (vertex1, vertex2) == link:
                return link
        return None

    def find_path(self, start_v: Vertex, stop_v: Vertex) -> tuple:
        """поиск кратчайшего маршрута из вершины start_v в вершину stop_v по алгоритму Дейкстры"""
        """маршрут возвращается в виде кортежа: ([вершины кратчайшего пути], [связи между вершинами])"""

        def connectivity(vertex1: Vertex, vertex2: Vertex):
            """вспомогательная функция для расчета матрицы связности, возвращает:
             - 0 если vertex1==vertex2
             - math.inf если vertex1 и vertex2 не являются соседями
             - длина связи Link.dist если vertex1 и vertex2 - соседи"""
            if vertex1 == vertex2:
                return 0
            else:
                link = self.get_link(vertex1, vertex2)
                return link.dist if link else inf

        def arg_min(T, S):
            amin = -1
            m = inf  # максимальное значение
            for i, t in enumerate(T):
                if t < m and i not in S:
                    m = t
                    amin = i

            return amin

        D = tuple(tuple(connectivity(vertexA, vertexB) for vertexB in self._vertex) for vertexA in self._vertex)
        N = len(D)  # число вершин в графе
        T = [inf] * N  # последняя строка таблицы
        v = self._vertex.index(start_v)  # стартовая вершина (нумерация с нуля)
        S = {v}  # просмотренные вершины
        T[v] = 0  # нулевой вес для стартовой вершины
        M = [0] * N  # оптимальные связи между вершинами

        while v != -1:  # цикл, пока не просмотрим все вершины
            for j, dw in enumerate(D[v]):  # перебираем все связанные вершины с вершиной v
                if j not in S:  # если вершина еще не просмотрена
                    w = T[v] + dw
                    if w < T[j]:
                        T[j] = w
                        M[j] = v  # связываем вершину j с вершиной v

            v = arg_min(T, S)  # выбираем следующий узел с наименьшим весом
            if v >= 0:  # выбрана очередная вершина
                S.add(v)  # добавляем новую вершину в рассмотрение

        start = self._vertex.index(start_v)
        end = self._vertex.index(stop_v)
        P = [end]
        while end != start:
            end = M[P[-1]]
            P.append(end)
        P.reverse()
        vertices = []
        for i in P:
            vertices.append(self._vertex[i])
        links = []
        for vertex1, vertex2 in zip(vertices[:-1], vertices[1:]):
            links.append(self.get_link(vertex1, vertex2))
        return vertices, links


map2 = LinkedGraph()
v1 = Vertex()
v2 = Vertex()
v3 = Vertex()
v4 = Vertex()
v5 = Vertex()

map2.add_link(Link(v1, v2))
map2.add_link(Link(v2, v3))
map2.add_link(Link(v2, v4))
map2.add_link(Link(v3, v4))
map2.add_link(Link(v4, v5))

assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"

map2.add_link(Link(v2, v1))
assert len(map2._links) == 5, "метод add_link() добавил связь Link(v2, v1), хотя уже имеется связь Link(v1, v2)"

path = map2.find_path(v1, v5)
s = sum([x.dist for x in path[1]])
assert s == 3, "неверная суммарная длина маршрута, возможно, некорректно работает объект-свойство dist"

assert issubclass(Station, Vertex) and issubclass(LinkMetro, Link), "класс Station должен наследоваться от класса Vertex, а класс LinkMetro от класса Link"

map2 = LinkedGraph()
v1 = Station("1")
v2 = Station("2")
v3 = Station("3")
v4 = Station("4")
v5 = Station("5")

map2.add_link(LinkMetro(v1, v2, 1))
map2.add_link(LinkMetro(v2, v3, 2))
map2.add_link(LinkMetro(v2, v4, 7))
map2.add_link(LinkMetro(v3, v4, 3))
map2.add_link(LinkMetro(v4, v5, 1))

assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"

path = map2.find_path(v1, v5)

assert str(path[0]) == '[1, 2, 3, 4, 5]', path[0]
s = sum([x.dist for x in path[1]])
assert s == 7, "неверная суммарная длина маршрута для карты метро"