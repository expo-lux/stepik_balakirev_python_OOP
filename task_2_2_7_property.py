class Stack(object):
    def __init__(self):
        self.top = None  # ссылка на первый добавленный объект односвязного списка
        self.__last = None

    def push(self, obj):
        """добавление объекта класса StackObj в конец односвязного списка"""
        if not self.top:
            self.top = self.__last = obj
        else:
            self.__last.next = obj
            self.__last = obj

    def pop(self):
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

    def get_data(self):
        """получение списка из объектов односвязного списка """
        pointer, result = self.top, []
        while pointer:
            result.append(pointer.data)
            pointer = pointer.next
        return result


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


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()
print(res)
st.pop()
res = st.get_data()
print(res)
st.pop()
res = st.get_data()
print(res)
st.pop()
res = st.get_data()
print(res)


