from collections.abc import Iterable


class Tuple(tuple):
    def __add__(self, obj):
        if isinstance(obj, Iterable):
            return Tuple(super().__add__(tuple(obj)))


t = Tuple([1, 2, 3])
t = t + "Python"
print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
t = (t + "Python") + "ООП"