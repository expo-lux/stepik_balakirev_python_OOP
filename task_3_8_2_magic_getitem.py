class Record:
    def __init__(self, **kwargs):
        self.attr = []
        for key, value in kwargs.items():
            self.__dict__[key] = value
            self.attr.append(key)

    def check_index(self, index):
        if index < 0 or index >= len(self.attr):
            raise IndexError('неверный индекс поля')

    def __getitem__(self, item):
        self.check_index(item)
        return getattr(self, self.attr[item])

    def __setitem__(self, key, value):
        self.check_index(key)
        setattr(self, self.attr[key], value)

r = Record(pk=1, title='Python ООП', author='Балакирев')
print(r.pk)
r[0] = 2  # доступ к полю pk
r[1] = 'Супер курс по ООП'  # доступ к полю title
r[2] = 'Балакирев С.М.'  # доступ к полю author
print(r[1])  # Супер курс по ООП
r[3]  # генерируется исключение IndexError
