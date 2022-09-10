class Wallet:
    def __init__(self, volume=100):
        self.volume = volume
        self.__cb: 'CentralBank' = None

    def cb_registered(self):
        if not self.cb:
            raise ValueError("Неизвестен курс валют.")

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value


class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money: Wallet):
        money.cb = cls

    @classmethod
    def USD2RUB(cls, usd: float):
        return cls.rates['rub'] * usd

    @classmethod
    def EUR2RUB(cls, eur: float):
        return (eur / cls.rates['euro']) * cls.rates['rub']


class MoneyR(Wallet):

    def __lt__(self, other: 'MoneyD'):
        self.cb_registered()
        return self.volume < self.cb.USD2RUB(other.volume)

    def __eq__(self, other: Wallet):
        self.cb_registered()
        if isinstance(other, MoneyE):
            return self.cb.EUR2RUB(other.volume) - 0.1 <= self.volume <= self.cb.EUR2RUB(other.volume) + 0.1


class MoneyE(Wallet):

    def __gt__(self, other: Wallet):
        self.cb_registered()
        if isinstance(other, MoneyR):
            return self.cb.EUR2RUB(self.volume) > other.volume
        elif isinstance(other, MoneyD):
            return self.cb.EUR2RUB(self.volume) > self.cb.USD2RUB(other.volume)
        elif isinstance(other, MoneyE):
            return self.volume > other.volume

    def __lt__(self, other: Wallet):
        self.cb_registered()
        if isinstance(other, MoneyR):
            return self.cb.EUR2RUB(self.volume) < other.volume
        elif isinstance(other, MoneyD):
            return self.cb.EUR2RUB(self.volume) < self.cb.USD2RUB(other.volume)
        elif isinstance(other, MoneyE):
            return self.volume < other.volume

    def __eq__(self, other):
        self.cb_registered()
        if isinstance(other, MoneyE):
            return self.cb.EUR2RUB(other.volume) - 0.1 <= self.cb.EUR2RUB(self.volume) <= self.cb.EUR2RUB(
                other.volume) + 0.1


class MoneyD(Wallet):

    def __ge__(self, other: 'MoneyE'):
        self.cb_registered()
        return self.cb.USD2RUB(self.volume) >= self.cb.EUR2RUB(other.volume)

    def __eq__(self, other):
        self.cb_registered()
        if isinstance(other, MoneyD):
            return self.cb.USD2RUB(other.volume) - 0.1 <= self.cb.USD2RUB(self.volume) <= self.cb.USD2RUB(
                other.volume) + 0.1


e = MoneyE()
d = MoneyD()
d1 = MoneyD()
r = MoneyR()
CentralBank.register(e)
CentralBank.register(d)
CentralBank.register(r)
print(e > d, e < d)
print(d > r, e < d)
print(d == d1)
print("End")
