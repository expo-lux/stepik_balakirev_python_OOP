class Translator:
    dic = {}

    def add(self, eng, rus):
        if eng in self.dic:
            self.dic[eng].append(rus)
        else:
            self.dic[eng] = [rus]

    def remove(self, eng):
        if eng in self.dic:
            self.dic.pop(eng)

    def translate(self, eng):
        return self.dic[eng] if eng in self.dic else []


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove("car")
lst = tr.translate("go")
print(*lst)
