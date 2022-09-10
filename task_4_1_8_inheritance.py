class Validator:
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value

    def _is_valid(self, data):
        return True

    def __call__(self, data):
        if not self._is_valid(data):
            raise ValueError('значение не прошло валидацию')


class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)

    def _is_valid(self, data):
        return type(data) == int and self._min_value <= data <= self._max_value


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)

    def _is_valid(self, data):
        return type(data) == float and self._min_value <= data <= self._max_value


integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
res1 = integer_validator(10)  # True
print(res1)
res2 = float_validator(10)  # исключение ValueError

