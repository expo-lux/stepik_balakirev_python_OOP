import time


class GeiserFilter:
    def __init__(self, date):
        self.date_locked = False
        self.date = date
        self.date_locked = True

    def __setattr__(self, key, value):
        if key == 'date':
            if not self.date_locked:
                super().__setattr__(key, value)
        else:
            super().__setattr__(key, value)


class Mechanical(GeiserFilter):
    pass


class Aragon(GeiserFilter):
    pass


class Calcium(GeiserFilter):
    pass


class GeyserClassic:
    MAX_DATE_FILTER = 100
    __check_filters = {1: 'Mechanical', 2: 'Aragon', 3: 'Calcium'}

    def __init__(self):
        self.__slots = {1: None, 2: None, 3: None}

    def __slot_is_empty(self, slot_num):
        return self.__slots[slot_num] is None

    @classmethod
    def __filter_is_suitable(cls, slot_num, filter):
        return filter.__class__.__name__ == cls.__check_filters[slot_num]

    @classmethod
    def __check_date(cls, filter):
        return 0 <= time.time() - filter.date <= cls.MAX_DATE_FILTER if filter else False

    def add_filter(self, slot_num, filter):
        if 1 <= slot_num <= 3 and self.__slot_is_empty(slot_num):
            if self.__filter_is_suitable(slot_num, filter):
                self.__slots[slot_num] = filter

    def remove_filter(self, slot_num):
        self.__slots[slot_num] = None

    def get_filters(self):
        return tuple(self.__slots.values())

    def water_on(self):
        all_slots_completed = all(map(lambda x: x is not None, self.__slots.values()))
        date_is_ok = all(map(self.__check_date, self.__slots.values()))
        return all_slots_completed and date_is_ok


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on()  # False
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on()  # True
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
my_water.add_filter(3, Calcium(time.time()))  # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time()))  # добавление в "чужой" слот также невозможно
