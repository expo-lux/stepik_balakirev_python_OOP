import sys


# здесь объявляйте классы
class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)


# считывание списка из входного потока
lst_in = ['Системный блок: 1500 75890.56',
'Системный блок: 1500 75890.56']
shop_items = {}
for item in lst_in:
    name = item.split(":")[0]
    weight, price = item.split(":")[1].strip().split()
    weight, price = float(weight), float(price)
    obj = ShopItem(name, weight, price)
    if obj in shop_items:
        shop_items[obj][1] += 1
    else:
        shop_items[obj] = [obj, 1]