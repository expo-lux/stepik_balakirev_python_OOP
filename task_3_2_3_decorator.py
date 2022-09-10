from random import sample
from random import randrange


class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.__chars = psw_chars
        self.__min = min_length
        self.__max = max_length

    def __call__(self, *args, **kwargs):
        cnt = randrange(self.__min, self.__max)
        return ''.join(sample(self.__chars, cnt))


rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)
lst_pass = [rnd() for i in range(3)]
print(lst_pass)
