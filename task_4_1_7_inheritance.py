class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Singleton.__instance:
            Singleton.__instance = super().__new__(cls)
        return Singleton.__instance


class Game(Singleton):
    name = ''
    def __init__(self, name=''):
        if Game.name:
            pass
        else:
            Game.name = name
        self.name = Game.name


a = Game("one")
print(a.name, id(a))
b = Game("two")
print(b.name, id(b))
