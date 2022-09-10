# здесь объявите класс TriangleChecker
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        def is_negative(*args):
            return any(map(lambda x: x <= 0, args))

        def invalid_type(*args):
            return {str} <= {type(par) for par in args}

        a, b, c = self.a, self.b, self.c
        if invalid_type(a, b, c) or is_negative(a, b, c):
            # если первое условие True то второе не оценивается
            return 1
        elif c > a + b or a > b + c or b > a + c:
            return 2
        else:
            return 3


a, b, c = map(int, input().split())  # эту строчку не менять
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
