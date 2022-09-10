class SoftList(list):
    def __setitem__(self, key, value):
        if (key < -len(self)) or key >= len(self):
            return False
        return super().__setitem__(key, value)

    def __getitem__(self, item):
        if (item < -len(self)) or item >= len(self):
            return False
        return super().__getitem__(item)

sl = SoftList("python")
print(sl[0]) # 'p'
print(sl[-1]) # 'n'
print(sl[6]) # False
print(sl[-7]) # False
sl[-7] = '0'
print(sl)
sl[-6] = 'A'
print(sl)
