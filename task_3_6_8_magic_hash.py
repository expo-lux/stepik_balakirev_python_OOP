class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = int(year)

    def __repr__(self):
        return f"{self.name} {self.author} {self.year}"

    def __eq__(self, other):  # объекты совпадают, если равны их хэши
        #используется множеством в ситуации, когда объект с таким же хэшем уже есть во множестве
        #если возвращается True - объект не добавляется во множество
        return hash(self) == hash(other)

    def __hash__(self):  # хэш определяется по атрибутам name, author
        return hash((self.name.lower(), self.author.lower()))


lst_bs = [BookStudy("Python", "Балакирев С.М.", 2020),
          BookStudy("Python ООП", "Балакирев С.М.", 2021),
          BookStudy("Python", "Балакирев С.М.", 2021)]
uniq = set(lst_bs)  # в множестве будет два объекта
