class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self.__count_objs = 0

    def push(self, obj):
        last = self[self.__count_objs - 1] if self.__count_objs > 0 else None
        if last:
            last.next = obj
        if self.top is None:
            self.top = obj
        self.__count_objs += 1

    def pop(self):
        if self.__count_objs == 0:
            return None

        last = self[self.__count_objs - 1]
        if self.__count_objs == 1:
            self.top = None
        else:
            self[self.__count_objs - 2].next = None

        self.__count_objs -= 1
        return last

    def __check_index(self, item):
        if type(item) != int or not (0 <= item < self.__count_objs):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_index(item)

        count = 0
        h = self.top
        while h and count < item:
            h = h.next
            count += 1
        return h

    def __setitem__(self, key, value):
        self.__check_index(key)
        obj = self[key]
        prev = self[key - 1] if key > 0 else None
        value.next = obj.next
        if prev:
            prev.next = value


st = Stack()
o = StackObj("1")
st.push(o) #элемент 0
st.push(o) #элемент 1
st.push(StackObj("2")) #элемент 2
print(st[0].data)
print(st[1].data)
print(st[2].data) #при попытке доступа к элементу 2 получаем ошибку AttributeError: 'NoneType' object has no attribute 'data'


# ​
# Код из видео-разбора валится с ошибкой на следующем тесте:
#
# st = Stack()
# o = StackObj("1")
# st.push(o)
# st.push(o)
# st.push(StackObj("2"))
# print(st[0].data)
# print(st[1].data)
# print(st[2].data) #AttributeError: 'NoneType' object has no attribute 'data'
#
#
# ​