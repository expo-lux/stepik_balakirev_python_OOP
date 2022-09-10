class IterColumn:
    def __init__(self, lst, column):
        self.__lst = lst
        self.__col = column
        self.__i = 0

    def __iter__(self):
        self.__i = 0
        return self

    def __next__(self):
        if self.__i < len(self.__lst):
            value = self.__lst[self.__i][self.__col]
            self.__i += 1
            return value
        else:
            raise StopIteration


class IterColumn2:
    def __init__(self, lst, column):
        self.__lst, self.__col = lst, column

    def __iter__(self):
        for i in range(len(self.__lst)):
            yield self.__lst[i][self.__col]


lst = [['x11', 'x12', 'x1N'],
       ['x21', 'x22', 'x2N'],
       ['x31', 'x32', 'x3N']]

it = IterColumn(lst, 0)
for x in it:
    print(x)

it = IterColumn2(lst, 0)
for x in it:
    print(x)

for x in it:
    print(x)
