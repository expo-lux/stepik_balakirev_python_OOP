class Box:
    def __init__(self, name, max_weight):
        self._max_weight = max_weight
        self._things = []
        self._name = name
        self._weight = 0

    @property
    def things(self):
        return self._things

    def add_thing(self, thing):
        if self._weight + thing[1] < self._max_weight:
            self._things.append(thing)
            self._weight += thing[1]
        else:
            raise ValueError('превышен суммарный вес вещей')


class BoxDefender:
    def __init__(self, box: Box):
        self._b: Box = box

    def __enter__(self):
        self.__temp = Box(self._b._name, self._b._max_weight)
        self.__temp._things = self._b._things[:]
        self.__temp._weight = self._b._weight
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self._b._things[:] = self.__temp._things
            self._b._weight = self.__temp._weight
        return False


b = Box('name', 2000)
assert b._name == 'name' and b._max_weight == 2000, "неверные значения атрибутов объекта класса Box"

b.add_thing(("1", 100))
b.add_thing(("2", 200))

try:
    with BoxDefender(b) as bb:
        bb.add_thing(("3", 1000))
        bb.add_thing(("4", 1900))
except ValueError:
    assert len(b._things) == 2

else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    with BoxDefender(b) as bb:
        bb.add_thing(("3", 100))
except ValueError:
    assert False, "возникло исключение ValueError, хотя, его не должно было быть"
else:
    assert len(b._things) == 3, "неверное число элементов в списке _things"
