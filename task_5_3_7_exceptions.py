digits = list(map(float, '1 2 3 4 5'.split()))  # эту строчку не менять (коллекцию digits также не менять)

# здесь создавайте объект класса

class TupleLimit(tuple):
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, args[0])
        max_length = args[1]
        if len(obj) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        return obj

    def __repr__(self):
        return " ".join(map(str, self))

try:
    a = TupleLimit(digits, 5)
    print(a)
except Exception as e:
    print(e)
