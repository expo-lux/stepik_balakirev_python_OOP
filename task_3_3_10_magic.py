class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"


class Recipe:
    def __init__(self, *args):
        self.__ing = list(args)

    def add_ingredient(self, ing: Ingredient):
        self.__ing.append(ing)

    def remove_ingredient(self, ing: Ingredient):
        self.__ing.remove(ing)

    def get_ingredients(self):
        return tuple(self.__ing)

    def __len__(self):
        return len(self.__ing)

recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
list(map(print, ings))
# [print(item) for item in ings]
n = len(recipe) # n = 3
