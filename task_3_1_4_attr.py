class Book:
    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key == 'title':
            if not type(value) == str:
                raise TypeError("Неверный тип присваиваемых данных.")
            else:
                self.__dict__[key] = value
        elif key == 'author':
            if not type(value) == str:
                raise TypeError("Неверный тип присваиваемых данных.")
            else:
                self.__dict__[key] = value
        elif key == 'pages':
            if not type(value) == int:
                raise TypeError("Неверный тип присваиваемых данных.")
            else:
                self.__dict__[key] = value
        elif key == 'year':
            if not type(value) == int:
                raise TypeError("Неверный тип присваиваемых данных.")
            else:
                self.__dict__[key] = value


book = Book("Python ООП", "Сергей Балакирев", 123, 2022)
