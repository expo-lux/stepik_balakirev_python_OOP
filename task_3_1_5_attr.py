class Product:
    __counter = 0
    attrs = {'name': [str], 'weight': [int, float], 'price': [int, float]}

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.__update_counter()
        self.__id = self.__counter

    @property
    def id(self):
        return self.__id

    @classmethod
    def __update_counter(cls):
        cls.__counter += 1

    def __setattr__(self, key, value):
        if key in self.attrs:
            if type(value) in self.attrs[key]:
                if key in ['weight', 'price']:
                    if value > 0:
                        return super().__setattr__(key, value)
                    else:
                        raise TypeError("Неверный тип присваиваемых данных.")
                else:
                    return super().__setattr__(key, value)
            else:
                raise TypeError("Неверный тип присваиваемых данных.")
        else:
            return super().__setattr__(key, value)

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")


class Shop:
    def __init__(self, name):
        self.__name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


book = Product("Python ООП", 100, 1024)
book2 = Product("Python ООП", 100, 1024)
book.id = 3
del book.id
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.title}, {p.practices}, {p.price}")
