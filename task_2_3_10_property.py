class StringValue:
    def __init__(self, min_length=2, max_length=50):
        self.__min = min_length
        self.__max = max_length

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def validate(self, value):
        return isinstance(value, str) and self.__min <= len(value) <= self.__max

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validate(value):
            setattr(instance, self.name, value)


class NumberValue:
    def __init__(self, max_val=10000):
        self.__max = max_val

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def validate(self, value):
        return type(value) in (float, int) and 0 <= value <= self.__max

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validate(value):
            setattr(instance, self.name, value)


class Thing:
    name = StringValue()
    weight = NumberValue()

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight):
        self.__max = max_weight
        self.__things = []
        self.__weight = 0

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        if self.__weight + thing.weight < self.__max:
            self.__things.append(thing)
            self.__weight += thing.weight

    def remove_thing(self, indx):
        if 0 <= indx <= len(self.things) - 1:
            self.__things.pop(indx)

    def get_total_weight(self):
        return self.__weight


bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
for t in bag.things:
    print(f"{t.title}: {t.practices}")