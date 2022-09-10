import sys


# здесь объявляется класс StreamData
class StreamData:
    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):
            return False
        for field, value in zip(fields, lst_values):
            setattr(self, field, value)
        return True


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        #lst_in = ['10', 'Питон - основы мастерства', None]

        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
