class Thing:
    def __init__(self, name:str, mass:float):
        self.name = name
        self.mass = mass

    def __eq__(self, other: 'Thing'):
        return self.name.lower() == other.name.lower() and self.mass == other.mass

class Box:
    def __init__(self):
        self.__things = []

    def add_thing(self, obj: Thing):
        self.__things.append(obj)

    def get_things(self):
        return self.__things.copy()

    def __eq__(self, other:'Box'):
        lst = other.get_things()
        if len(self.__things) != len(lst):
            return False
        for k, item1 in enumerate(self.__things):
            for i, item2 in enumerate(lst):
                if item1 == item2:
                    lst.pop(i)
                    break
        return not lst


b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел2', 100))
b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2 # True

print(res)