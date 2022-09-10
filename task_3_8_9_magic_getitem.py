class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight):
        self.__max = max_weight
        self.__things = []
        self.__weight = 0

    def add_thing(self, thing):
        if self.__weight + thing.weight <= self.__max:
            self.__things.append(thing)
            self.__weight += thing.weight
        else:
            raise ValueError('превышен суммарный вес предметов')

    def check_index(self, index):
        if not 0 <= index <= len(self.__things):
            raise IndexError('неверный индекс')

    def __getitem__(self, index):
        self.check_index(index)
        return self.__things[index]

    def __setitem__(self, index, value):
        self.check_index(index)
        diff = value.weight - self.__things[index].weight
        if self.__weight + diff <= self.__max:
            self.__things[index] = value
            self.__weight += diff
        else:
            raise ValueError('превышен суммарный вес предметов')

    def __delitem__(self, index):
        self.check_index(index)
        weight = self[index].weight
        self.__things.pop(index)
        self.__weight -= weight



b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

try:
    b.add_thing(Thing('рубашка', 500))
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

assert b[0].name == 'книга' and b[
    0].weight == 100, "атрибуты name и weight объекта класса Thing принимают неверные значения"

t = Thing('Python', 20)
b[1] = t
assert b[1].name == 'Python' and b[
    1].weight == 20, "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"

del b[0]
assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"

try:
    t = b[2]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

b[0] = Thing('рубашка', 500)

try:
    b[0] = Thing('рубашка', 800)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"