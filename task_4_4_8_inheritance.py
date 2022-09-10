class Aircraft:
    def __init__(self, model, mass, speed, top):
        self.valid_string(model)
        self.valid_positive(mass)
        self.valid_positive(speed)
        self.valid_positive(top)
        self._model, self._mass, self._speed, self._top = model, mass, speed, top

    @staticmethod
    def valid_string(value):
        if type(value) != str:
            raise TypeError('неверный тип аргумента')

    @staticmethod
    def valid_positive(value):
        if (not type(value) in (float, int)) or value <= 0:
            raise TypeError('неверный тип аргумента')

    @staticmethod
    def valid_integer(value):
        if type(value) != int:
            raise TypeError('неверный тип аргумента')


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self.valid_integer(chairs)
        self.valid_positive(chairs)
        self._chairs = chairs


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self.valid_dict(weapons)
        self._weapons = weapons

    @classmethod
    def valid_dict(cls, d):
        if type(d) == dict:
            for key, value in d.items():
                cls.valid_string(key)
                cls.valid_positive(value)
                cls.valid_integer(value)
        else:
            raise TypeError('неверный тип аргумента')

planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]

print(planes)