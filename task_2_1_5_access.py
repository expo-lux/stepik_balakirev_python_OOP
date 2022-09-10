class Money(object):
    def __init__(self, money: int):
        self.__money = money

    @classmethod
    def __check_money(cls, money):
        return type(money) == int and 0 <= money

    def get_money(self) -> int:
        return self.__money

    def add_money(self, mn):
        self.set_money(self.get_money() + mn.get_money())

    def set_money(self, money: int):
        if self.__check_money(money):
            self.__money = money
