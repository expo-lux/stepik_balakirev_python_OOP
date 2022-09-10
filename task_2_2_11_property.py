class PhoneNumber:
    DIGITS = 11

    def __init__(self, number, fio):
        self.number = number
        self.fio = fio

    @classmethod
    def check_number(cls, value):
        return type(value) is int and len(str(value)) == cls.DIGITS

    def init(self):
        self.number = 11111111111
        self.fio = ''

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if self.check_number(value):
            self.__number = value

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, value):
        self.__fio = value


class PhoneBook:
    def __init__(self):
        self.__phones = []

    def add_phone(self, phone):
        self.__phones.append(phone)

    def remove_phone(self, indx):
        self.__phones.pop(indx)

    def get_phone_list(self):
        return self.__phones

p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
print(phones)