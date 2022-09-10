class Animal:
    def __init__(self, name, old):
        self.name = name
        self.old = old


class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight

    def get_info(self):
        print(f"{self.name}: {self.old}, {self.color}, {self.weight}")


class Dog(Animal):
    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size: tuple = size

    def get_info(self):
        
        print(f"{self.name}: {self.old}, {self.breed}, {self.size[0]}, {self.size[1]}")



cat = Cat('cat', 5, 'green', 2)
cat.get_info()