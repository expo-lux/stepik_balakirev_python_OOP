class StackObj(object):
    def __init__(self, data):
        self.data = data
        self.next = None

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

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class Stack(object):
    def __init__(self):
        self.top = None  # ссылка на первый добавленный объект односвязного списка
        self.__last = None

    def push_back(self, obj: StackObj):
        """добавление объекта класса StackObj в конец односвязного списка (если его там еще нет)"""
        if self.contains(obj):
            raise Exception("Элемент уже есть в стеке")
        if not self.top:
            self.top = self.__last = obj
        else:
            self.__last.next = obj
            self.__last = obj

    def pop_back(self):
        """извлечение последнего объекта с его удалением из односвязного списка"""
        if self.top:
            if self.top == self.__last:  # извлечение последнего объекта
                self.top = self.__last = None
            else:
                pointer = self.top
                while pointer:
                    if pointer.next == self.__last:
                        pointer.next = None
                        self.__last = pointer
                        break
                    else:
                        pointer = pointer.next
        else:
            raise IndexError("Pop from empty stack")

    def contains(self, obj):
        pointer, result = self.top, False
        while pointer:
            if pointer is obj:
                return True
            else:
                pointer = pointer.next
        return False

    def get_data(self):
        """получение списка из объектов односвязного списка """
        pointer, result = self.top, []
        while pointer:
            result.append(pointer.data)
            pointer = pointer.next
        return result

    @staticmethod
    def check_type(obj):
        if isinstance(obj, StackObj):
            return True
        else:
            raise TypeError("Invalid type")

    def __add__(self, other):
        self.check_type(other)
        self.push_back(other)
        return self

    def __mul__(self, other):
        for item in other:
            self.push_back(StackObj(item))
        return self

    def __str__(self):
        return str(self.get_data())


s = Stack()
obj = StackObj("x")
s.push_back(obj)
s.push_back(obj)