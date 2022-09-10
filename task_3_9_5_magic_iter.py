class Person:
    def __init__(self,fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.__it = None
        self.__attr = ('fio', 'job', 'old', 'salary', 'year_job')

    def __iter__(self):
        self.__it = iter(list(self.__dict__.values())[:-2])
        return self.__it

    def __next__(self):
        return next(self.__it)

    @staticmethod
    def check_index(index):
        return 0 <= index <= 4

    def __getitem__(self, index):
        self.check_index(index)
        return getattr(self, self.__attr[index])

    def __setitem__(self, index, value):
        self.check_index(4)
        setattr(self, self.__attr[index], value)




p = Person('1', '2', '3', '4', '5')
for attr in p:
    print(attr)

pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
pers[5] = 123 # IndexError