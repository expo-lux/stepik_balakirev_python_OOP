class Telecast:
    def __init__(self, id, name, duration):
        self.uid = id
        self.name = name
        self.duration = duration

    @property
    def uid(self):
        return self.__id

    @classmethod
    def is_valid(cls, value):
        return type(value) is int

    @uid.setter
    def uid(self, value):
        if self.is_valid(value):
            self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        self.__duration = value


class TVProgram:
    def __init__(self, channel):
        self.__channel = channel
        self.items = []

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx):
        for i in self.items:
            if i.uid == indx:
                self.items.remove(i)
                break

pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
for t in pr.items:
    print(f"{t.title}: {t.duration}")