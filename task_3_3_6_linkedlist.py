class ObjList:
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def __str__(self):
        return self.__data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


class LinkedList:
    def __init__(self):
        self.head: ObjList = None
        self.tail: ObjList = None
        self.__length = 0

    def __len__(self):
        return self.__length

    def __call__(self, indx):
        """возвращает строку __data, хранящуюся в объекте класса ObjList, расположенного под индексом indx"""
        if indx < len(self):
            count, pointer = 0, self.head
            while count < indx:
                pointer = pointer.get_next()
                count += 1
            return pointer.get_data()
        else:
            raise IndexError("LinkedList index out of range")

    def add_obj(self, obj: ObjList):
        """добавление нового объекта obj класса ObjList в конец связного списка"""
        if self.head is None and self.tail is None:
            self.head = self.tail = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

        self.__length += 1

    def remove_obj(self, indx):
        if indx < len(self):
            count, pointer = 0, self.head
            while count < indx:
                pointer = pointer.get_next()
                count += 1

            prev: ObjList = pointer.get_prev()
            next: ObjList = pointer.get_next()

            if prev is None:
                if next is None:
                    # удаляем единственный элемент
                    self.head = self.tail = None
                else:
                    # удаляем первый элемент
                    next.set_prev(None)
                    self.head = next
            else:
                if next is None:
                    # удаляем крайний элемент
                    prev.set_next(None)
                    self.tail = prev
                else:
                    # удаляем элемент из середины
                    prev.set_next(next)
                    next.set_prev(prev)
            self.__length -= 1
        else:
            raise IndexError("LinkedList index out of range")


lst = LinkedList()
lst.add_obj(ObjList("данные 0"))
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
for i in range(len(lst)):
    print(lst(i))
print(len(lst))
lst.remove_obj(1)
for i in range(len(lst)):
    print(lst(i))
print(lst.tail)
print(lst.head)


