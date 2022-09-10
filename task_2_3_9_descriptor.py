class StringValue:
    def __init__(self, min_length=2, max_length=50):
        self.__min = min_length
        self.__max = max_length

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def validate(self, value):
        return isinstance(value, str) and self.__min <= len(value) <= self.__max

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validate(value):
            setattr(instance, self.name, value)



class PriceValue:
    def __init__(self, max_val=10000):
        self.__max = max_val

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def validate(self, value):
        return type(value) in (float, int) and 0 <= value <= self.__max

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validate(value):
            setattr(instance, self.name, value)


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        self.init()
        self.name = name
        self.price = price

    def init(self):
        self.name = 'undefined'
        self.price = 0


class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)

p = Product('1', 1000)
shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.title}: {p.price}")
