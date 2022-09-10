from abc import ABC, abstractmethod

# здесь объявляйте классы

class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        """ """
    @abstractmethod
    def pop_back(self):
        """ """


class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None
        self._data = data
        self._next = None

    @staticmethod
    def check_next(obj):
        return obj is None or isinstance(obj, StackObj)

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if self.check_next(obj):
            self.__next = obj
            self._next = self.__next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value
        self._data = self.__data


class Stack(StackInterface):
    def __init__(self):
        self._top = None  # ссылка на первый добавленный объект односвязного списка
        self.__last = None

    def push_back(self, obj: StackObj):
        """добавление объекта класса StackObj в конец односвязного списка (если его там еще нет)"""
        if self.contains(obj):
            raise Exception("Элемент уже есть в стеке")
        if not self._top:
            self._top = self.__last = obj
        else:
            self.__last.next = obj
            self.__last = obj

    def pop_back(self):
        """извлечение последнего объекта с его удалением из односвязного списка"""
        if self._top:
            if self._top == self.__last:  # извлечение последнего объекта
                temp = self._top
                self._top = self.__last = None
                return temp
            else:
                pointer = self._top
                while pointer:
                    if pointer.next == self.__last:
                        temp = self.__last
                        pointer.next = None
                        self.__last = pointer
                        return temp
                    else:
                        pointer = pointer.next
        else:
            return None

    def contains(self, obj):
        pointer, result = self._top, False
        while pointer:
            if pointer is obj:
                return True
            else:
                pointer = pointer.next
        return False


    @staticmethod
    def check_type(obj):
        if isinstance(obj, StackObj):
            return True
        else:
            raise TypeError("Invalid type")

    def __str__(self):
        return str(self.get_data())


assert issubclass(Stack, StackInterface), "класс Stack должен наследоваться от класса StackInterface"

try:
    a = StackInterface()
    a.pop_back()
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове абстрактного метода класса StackInterface"


st = Stack()
assert st._top is None, "атрибут _top для пустого стека должен быть равен None"

obj_top = StackObj("obj")
st.push_back(obj_top)

assert st._top == obj_top, "неверное значение атрибута _top"

obj = StackObj("obj")
st.push_back(obj)

n = 0
h = st._top
while h:
    assert h._data == "obj", "неверные данные в объектах стека"
    h = h._next
    n += 1

assert n == 2, "неверное число объектов в стеке (или структура стека нарушена)"

del_obj = st.pop_back()
assert del_obj == obj, "метод pop_back возвратил неверный объект"

del_obj = st.pop_back()
assert del_obj == obj_top, "метод pop_back возвратил неверный объект"

assert st._top is None, "неверное значение атрибута _top"