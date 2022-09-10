class InputValues:#декоратор с параметром
    def __init__(self, render):
    # render - ссылка на функцию или объект для преобразования (параметр класса-декоратора)
        self.__render = render

    def __call__(self, func):  # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            res: str = func(*args, **kwargs)
            render = self.__render()
            return [render(item) for item in res.split()]

        return wrapper


class RenderDigit():#функтор
    def __call__(self, value):
        if value.startswith('-'):
            return int(value) if str.isdigit(value[1:]) else None
        else:
            return int(value) if str.isdigit(value) else None


@InputValues(render=RenderDigit)
def input_dg(*args, **kwargs):
    return input(*args, **kwargs)

res = input_dg()
print(res)
