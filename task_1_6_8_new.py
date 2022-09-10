# здесь объявляйте класс SingletonFive
class SingletonFive:
    counter = 0
    fifth = None

    def __new__(cls, *args, **kwargs):
        cls.counter += 1
        # print(cls)
        # print(cls.mro())
        # print(*args, **kwargs)
        if SingletonFive.counter == 5:
            cls.fifth = super().__new__(cls)
            return cls.fifth
        elif SingletonFive.counter < 5:
            return super().__new__(cls)
        elif SingletonFive.counter > 5:
            return cls.fifth


    def __del__(self):
        SingletonFive.counter -= 1


    def __init__(self, name):
        self.name = name

a = SingletonFive('1')
b = SingletonFive('2')
c = SingletonFive('3')
del b
d = SingletonFive('4')
# objs=[SingletonFive(str(n)) for n in range(10)]  # эту строчку не менять
# for i in objs:
#     print(i)