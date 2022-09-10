class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.__it = None

    def __gen(self):
        for i in range(len(self.lst)):
            for j in range(i + 1):
                yield i, j

    def __iter__(self):
        self.__it = self.__gen()
        return self

    def __next__(self):
        i, j = next(self.__it)
        return self.lst[i][j]


class TriangleListIterator2:
    def __init__(self, lst):
        self.lst = sum(lst, [])

    def __iter__(self):
        return iter(self.lst)

lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11'],
       ['x20', 'x21', 'x22', 'x23', 'x24'],
       ['x30', 'x31', 'x32', 'x33']]

it = TriangleListIterator2(lst)
for i in it:
    print(i)
it = TriangleListIterator(lst)
for j in it:
    print(j)
