class IntPositiveValue:
    @classmethod
    def validate(cls, value):
        if (not type(value) in (int,)) or value < 0:
            raise ValueError('некорректные координаты и параметры прямоугольника')

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)


class ValidatorString:
    min_length = IntPositiveValue()
    max_lenght = IntPositiveValue()

    def __init__(self, min_length, max_length, chars):
        self.min_length, self.max_lenght, self.__chars = min_length, max_length, chars

    def is_valid(self, string):
        string_valid = bool(set(self.__chars) & set(string)) if self.__chars else True
        if not (isinstance(string, str) and self.min_length <= len(string) <= self.max_lenght
                and string_valid):
            raise ValueError('недопустимая строка')


class LoginForm:
    def __init__(self, login_validator: ValidatorString, password_validator: ValidatorString):
        self.__login_validator, self.__password_validator = login_validator, password_validator
        self._login = self._password = ''

    def form(self, request: dict):
        if 'login' in request and 'password' in request:
            self.__login_validator.is_valid(request['login'])
            self.__password_validator.is_valid(request['password'])
            self._login = request['login']
            self._password = request['password']
        else:
            raise TypeError('в запросе отсутствует логин или пароль')


login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = input().split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)
