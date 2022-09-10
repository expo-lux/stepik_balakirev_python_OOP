class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(0)

    def get_list(self):
        return [f"{i.title}: {i.price}" for i in self.goods]

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Table(Product):
    pass

class TV(Product):
    pass

class Notebook(Product):
    pass

class Cup(Product):
    pass

tv1 = TV("samsung", 1111)
tv2 = TV("LG", 1234)
table = Table("ikea", 2345)
n1= Notebook("msi", 5433)
n2 = Notebook("apple", 542)
c = Cup("keepcup", 43)

cart = Cart()
cart.add(tv1)
cart.add(tv2)
cart.add(table)
cart.add(n1)
cart.add(n2)
cart.add(c)
print(cart.get_list())