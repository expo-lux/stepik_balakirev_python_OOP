# здесь объявляйте класс


text = input()   # эту строчку не менять

# здесь создавайте объекты класса и обрабатывайте строку text

class Morph:
    def __init__(self, *args):
        self.lst = list(args)

    def add_word(self, word):
        self.lst.append(word)

    def get_words(self):
        return tuple(self.lst)

    def __eq__(self, other: str):
        return other.lower() in self.lst

    def __contains__(self, item: str):
        return self.__eq__(item)


dict_words = [Morph('связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях'),
              Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами',
                    'формулах'),
              Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам',
                    'векторами', 'векторах'),
              Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам',
                    'эффектами', 'эффектах'),
              Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')]

words = [word.strip("–?!,.;") for word in text.split()]
count = sum([1 if word in obj else 0 for word in words for obj in dict_words])
print(count)
