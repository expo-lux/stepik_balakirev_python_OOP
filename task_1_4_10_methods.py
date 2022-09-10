import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
# lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for item in data:
            data = item.split()
            DataBase.lst_data.append(dict(zip(DataBase.FIELDS, data)))

    def select(self, a, b):
        return DataBase.lst_data[a:b+1]


db = DataBase()
db.insert(lst_in)
print(db.select(1, 2))
