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

    def __repr__(self):
        return str(self.data)


class Stack(object):
    def __init__(self):
        self.top = None  # ссылка на первый добавленный объект односвязного списка
        self.__last = None
        self.__length = 0

    def push(self, obj: StackObj):
        """добавление объекта класса StackObj в конец односвязного списка (если его там еще нет)"""
        if obj in self:
            raise Exception("Элемент уже есть в стеке")
        if not self.top:
            self.top = self.__last = obj
        else:
            self.__last.next = obj
            self.__last = obj

        self.__length += 1

    def pop(self):
        """извлечение последнего объекта с его удалением из односвязного списка"""
        if self.top:
            temp = self.__last
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
            self.__length -= 1
            return temp
        else:
            raise IndexError("Pop from empty stack")

    def __contains__(self, obj):
        pointer, result = self.top, False
        while pointer:
            if pointer is obj:
                return True
            else:
                pointer = pointer.next
        return False

    def __get_data(self):
        """получение кортежа из объектов односвязного списка """
        pointer, result = self.top, tuple()
        while pointer:
            result += pointer.data,
            pointer = pointer.next
        return result

    def __len__(self):
        return self.__length

    @staticmethod
    def check_type(obj):
        if isinstance(obj, StackObj):
            return True
        else:
            raise TypeError("Invalid type")

    def __add__(self, other):
        self.check_type(other)
        self.push(other)
        return self

    def __mul__(self, other):
        for item in other:
            self.push(StackObj(item))
        return self

    def __repr__(self):
        return str(self.__get_data())

    def check_index(self, index):
        if type(index) != int or index < 0 or index >= len(self):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.check_index(item)
        pointer, i = self.top, 0
        while i != item:
            pointer = pointer.next
            i += 1
        return pointer

    def __setitem__(self, index, obj):
        self.check_index(index)
        self[index].data = obj.data


st = Stack()
print(st)
st.push(StackObj("obj1"))
print(st)
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
print(st[2].data) # obj3
print(st[1].data) # new obj2
res = st[3] # исключение IndexError