class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top: StackObj = None  # ссылка на первый элемент стека
        self.__length = 0

    def _check_index(self, index):
        if not (type(index) == int and 0 <= index < len(self)):
            raise IndexError('неверный индекс')

    def __bool__(self):
        return True if len(self) > 0 else False

    def push_back(self, obj: StackObj):
        """ добавления нового объекта obj в конец стека"""
        last = self.__getelem(len(self) - 1) if len(self) > 0 else None
        if last:
            last.next = obj
        else:
            self.top = obj
        self.__length += 1

    def pop(self) -> str:
        """Удаляет элемент с конца стека и возвращает его"""
        prev = self.__getelem(len(self) - 2) if len(self) > 1 else None
        if prev:
            result = prev.next
            prev.next = None
        else:
            if self.top:
                result = self.top
                self.top = None
            else:
                raise IndexError("Pop from empty stack")
        self.__length -= 1
        return result.data

    def push_front(self, obj: StackObj):
        """ добавление нового объекта obj в начало стека"""
        if self.top:
            top = self.top
            self.top = obj
            obj.next = top
        else:
            self.top = obj
        self.__length += 1

    def __getelem(self, index: int) -> StackObj:
        """Возвращает StackObj из стека по индексу"""
        self._check_index(index)
        pointer, count = self.top, 0
        while pointer and count < index:
            pointer = pointer.next
            count += 1
        return pointer

    def __getitem__(self, index: int):
        """Возвращает данные StackObj.data из стека по индексу"""
        return self.__getelem(index).data

    def __setitem__(self, index: int, value: str):
        """Записывает данные в объект по индексу"""
        self._check_index(index)
        self.__getelem(index).data = value

    def __len__(self) -> int:
        """Кол-во элементов в стеке"""
        return self.__length

    def __iter__(self):
        pointer = self.top
        while pointer:
            yield pointer
            pointer = pointer.next


st = Stack()
st.push_back(StackObj("1"))
st.push_front(StackObj("2"))

for obj in st:
    print(obj.data)
print("-"*30)
print("Pop " + st.pop())
print("-"*30)
for obj in st:
    print(obj.data)
print("-"*30)
st.push_back(StackObj("sdff"))
for obj in st:
    print(obj.data)