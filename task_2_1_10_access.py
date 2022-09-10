class ObjList:
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

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
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        """добавление нового объекта obj класса ObjList в конец связного списка"""
        if self.head is None and self.tail is None:
            self.head = self.tail = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

    def remove_obj(self):
        """удаление крайнего объекта из связного списка"""
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)

    def get_data(self) -> list:
        """получение списка из строк локального свойства __data всех объектов связного списка"""
        pointer, result = self.head, []
        while pointer:
            result.append(pointer.get_data())
            pointer = pointer.get_next()
        return result

lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()
print(res)

lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.remove_obj()
res = lst.get_data()
print(res)
lst.add_obj(ObjList(12))
res = lst.get_data()
print(res)
lst.remove_obj()
lst.remove_obj()
lst.remove_obj()
res = lst.get_data()
print(res)
