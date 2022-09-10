vector_log = []  # наименование (vector_log) в программе не менять!


# # здесь объявляйте декоратор и все что с ним связано
# def integer_params_decorated(func):
#     def wrapper(*args, **kwargs):
#         for arg in args[1:]:
#             if not type(arg) == int:
#                 raise TypeError("аргументы должны быть целыми числами")
#         for k, v in kwargs.items():
#             if not type(v) == int:
#                 raise TypeError("аргументы должны быть целыми числами")
#         return func(*args, **kwargs)
#     return wrapper
#
# def class_log(l: list):
#     def decorator(cls):
#             methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
#             for k, v in methods.items():
#                 setattr(cls, k, integer_params_decorated(v))
#     return decorator


#
# # здесь объявляйте функцию-декоратор
# def integer_params_decorated(func, l:list):
#     def wrapper(self, *args, **kwargs):
#         print(func)
#         dir(func)
#         l.append(self)
#         return func(*args, **kwargs)
#     return wrapper
#
#
# def class_log(l: list):
#     def inner(cls):
#         methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
#         for k, v in methods.items():
#             setattr(cls, k, integer_params_decorated(v, l))
#
#         return cls
#     return inner


# здесь объявляйте функцию-декоратор
def integer_params_decorated(func, attr: str, log: list):
    def wrapper(*args, **kwargs):
        log.append(attr)
        return func(*args, **kwargs)

    return wrapper


def class_log(l: list):
    def inner(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, integer_params_decorated(v, k, l))

        return cls

    return inner


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


v = Vector(1, 2, 3)
v[0] = 10
print(v[1])
print(vector_log)
