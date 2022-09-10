class StackObjDescr:
    def __set_name__(self, owner, name):
        self.name = f"_{owner.__name__}__{name}"

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class StackObj:
    data = StackObjDescr()
    next = StackObjDescr()

    def __init__(self, data: str) -> None:
        self.data = data
        self.next = next = None


class Stack:
    def __init__(self) -> None:
        self.top    = None
        self.length = 0

    def get_stack_end_obj(self, prev_last: bool = False) -> StackObj:
        obj = self.top
        for i in range(self.length-1 - prev_last):
            obj = obj.next
        return obj

    def push_back(self, obj: StackObj) -> None:
        if self.length == 0:
            self.top = obj
        else:
            lastObj = self.get_stack_end_obj()
            lastObj.next = obj
        self.length += 1

    def pop_back(self) -> None:
        if self.length:
            if self.length == 1:
                self.top = None
            else:
                prevLastObj = self.get_stack_end_obj(prev_last = True)
                prevLastObj.next = None
            self.length -= 1

    def __add__(self, obj: StackObj) -> "Stack":
        self.push_back(obj)
        return self

    def __mul__(self, lst: list) -> "Stack":
        tempObj = StackObj(lst[0])
        self.push_back(tempObj)
        for i in range(1, len(lst)):
            tempObj.next = tempObj = StackObj(lst[i])
            self.length += 1
        return self


print("start")
s, obj = Stack(), StackObj("1")
s.push_back(StackObj("some"))
s.push_back(obj)
s.push_back(obj)
s.push_back(obj) #добавляем obj еще раз
s.pop_back() #здесь зависает в бесконечном цикле
print("the end")

