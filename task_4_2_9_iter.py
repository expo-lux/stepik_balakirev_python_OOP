class IteratorAttrs:
    def __iter__(self):
        for key, value in self.__dict__.items():
            yield key, value


class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        self.model, self.size, self.memory = model, size, memory


phone = SmartPhone('Nokia 228', (4, 5), 128)
for attr, value in phone:
    print(attr, value)
