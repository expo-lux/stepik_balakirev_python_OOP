class Thing:
    id = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Thing.id = Thing.id + 1
        self.id = Thing.id
        self.weight = self.dims = self.memory = self.frm = None

    def get_data(self):
        return self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm


class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm


a = Thing('a', 2)
print(a.id)
b = Thing('b', 2)
print(b.id)
table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data())
print(*book.get_data())