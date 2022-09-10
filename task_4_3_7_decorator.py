# здесь объявляйте функцию-декоратор
def integer_params_decorated(func):
    def wrapper(*args, **kwargs):
        for arg in args[1:]:
            if not type(arg) == int:
                raise TypeError("аргументы должны быть целыми числами")
        for k, v in kwargs.items():
            if not type(v) == int:
                raise TypeError("аргументы должны быть целыми числами")
        return func(*args, **kwargs)
    return wrapper


def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls


@integer_params
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    @classmethod
    def some_class_func(cls, param):
        print(param)

    @staticmethod
    def some_static_method(param):
        print(param)

    def set_coords(self, *coords, reverse=False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]

vector = Vector(1, 2, 3)
# print(callable(Vector.some_class_func))
# print(callable(Vector.some_static_method))
print(vector[0])
print(vector[1])
print(vector[2])
vector[0], vector[1], vector[2] = 10, 20, 30

vector[1] = 20.4 # TypeError
