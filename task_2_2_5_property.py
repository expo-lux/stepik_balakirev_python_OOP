class Car:
    def __init__(self):
        self.model = "Lada"

    @staticmethod
    def check_model(model):
        return type(model) == str and 2 <= len(model) <= 100

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if self.check_model(value):
            self.__model = value


Toyota = Car()
print(Toyota.model)