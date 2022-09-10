class PrimaryKeyError(Exception):
    def __init__(self, **kwargs):
        if len(kwargs) == 0:
            self.msg = "Первичный ключ должен быть целым неотрицательным числом"
        else:
            self.msg = f"Значение первичного ключа {list(kwargs.keys())[0]} = {list(kwargs.values())[0]} недопустимо"
        super().__init__()

    def __str__(self):
        return self.msg


try:
    raise PrimaryKeyError(id=-10.5)
except PrimaryKeyError as e:
    print(e)
