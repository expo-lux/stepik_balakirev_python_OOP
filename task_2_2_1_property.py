class Person:
    def __init__(self, old, height):
        self.old = old
        self.height = height

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old

    old = property(get_old, set_old)

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    name = property(get_name)
    name = name.setter(set_name)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value


John = Person(25, 175)
print(John.height)
John.name = "John"