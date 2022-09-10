class Note:
    __cyrillic_notes = 'до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'

    @classmethod
    def validate(cls, name):
        if not name in cls.__cyrillic_notes:
            raise ValueError('недопустимое значение аргумента')

    def __init__(self, name, ton=0):
        # assert False, f'{name} {ton}'
        self.validate(name)
        if not ton in (1, 0, -1):
            raise ValueError('недопустимое значение аргумента')
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if key == '_name':
            self.validate(value)
        elif key == '_ton':
            if not value in (1, 0, -1):
                raise ValueError('недопустимое значение аргумента')
        return super().__setattr__(key, value)


class Notes:
    __instance = None
    __slots__ = '_do', '_re', '_mi', '_fa', '_solt', '_la', '_si'

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self._do, self._re, self._mi, self._fa, self._solt, self._la, self._si = Note('до'), Note('ре'), Note(
            'ми'), Note('фа'), Note('соль'), Note('ля'), Note('си')

    def validate_index(self, index):
        if type(index) != int or index < 0 or index > 6:
            raise IndexError('недопустимый индекс')

    def __getitem__(self, index):
        self.validate_index(index)
        return self.__getattribute__(self.__slots__[index])


n = Notes()
n[1]._name = 'ls'
print('x')
