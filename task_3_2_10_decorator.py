class InputDigits:
    def __init__(self, func):
        self.__f = func

    def __call__(self, *args, **kwargs):
        result = self.__f(*args, **kwargs)
        return list(map(int, result.split()))


@InputDigits
def input_dg(*args, **kwargs):
    return input(*args, **kwargs)


res = input_dg()
