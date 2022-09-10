from random import randint


class Cell:
    __repr = ('-', 'X', 'O')

    def __init__(self):
        self.value = TicTacToe.FREE_CELL

    def __bool__(self):
        """Возвращает True, если клетка свободна (value 0), False в противном случае"""
        return True if self.value == TicTacToe.FREE_CELL else False

    def __repr__(self):
        return self.__repr[self.value]


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self, size=3):
        self.size = size

    def generate_slices(self):
        for i in range(self.size):
            yield self[i, :]
        for j in range(self.size):
            yield self[:, j]
        yield tuple(self[i, j]
                    for i in range(self.size)
                    for j in range(self.size)
                    if i == j)
        yield tuple(self[i, j]
                    for i in range(self.size)
                    for j in range(self.size)
                    if i == self.size - 1 - j)

    def check_index(self, index):
        if not (type(index) in (int, float) and 0 <= index < self.size):
            raise IndexError('неверный индекс клетки')

    def __set_board(self):
        self.pole = tuple(tuple(Cell() for j in range(self.size)) for i in range(self.size))
        self.__free_cell_counter = self.size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        self.__set_board()

    def __getitem__(self, item: tuple):
        val1, val2 = item
        if isinstance(val2, slice):  # все элементы строки val1
            self.check_index(val1)
            return tuple(item.count for item in self.pole[val1])
        elif isinstance(val1, slice):  # все элементы столбца val2
            self.check_index(val2)
            return tuple(self.pole[i][val2].count for i in range(self.size))
        elif isinstance(val2, int) and isinstance(val1, int):
            self.check_index(val1)
            self.check_index(val2)
            return self.pole[val1][val2].count

    def __setitem__(self, indexes: tuple, value: int):
        row, col = indexes
        self.check_index(row)
        self.check_index(col)
        self.pole[row][col].count = value

    @property
    def is_human_win(self):
        for slc in self.generate_slices():
            if all(map(lambda item: item == self.HUMAN_X, slc)):
                return True
        return False

    @property
    def is_computer_win(self):
        for slc in self.generate_slices():
            if all(map(lambda item: item == self.COMPUTER_O, slc)):
                return True
        return False

    @property
    def is_draw(self):
        return not (self.is_computer_win or self.is_human_win) and self.__free_cell_counter == 0

    def init(self):
        for row in self.pole:
            for col in row:
                col.value = self.FREE_CELL
        self.__free_cell_counter = self.size ** 2

    def show(self):
        print(' ', ' '.join(tuple(str(i) for i in range(self.size))))
        for i, v in enumerate(self.pole):
            print(i, *v)

    def human_go(self):
        while True:
            indexes = input("Куда поставить крестик (две цифры через пробел, например '2 0')? ").split()
            indexes = int(indexes[0]), int(indexes[1])
            if game[indexes] == self.FREE_CELL:
                break
            else:
                print("Эта ячейка уже занята")
        game[indexes] = self.HUMAN_X
        print()
        self.__free_cell_counter -= 1

    def computer_go(self):
        indexes = randint(0, self.size - 1), randint(0, self.size - 1)
        while game[indexes] != self.FREE_CELL:
            indexes = randint(0, self.size - 1), randint(0, self.size - 1)
        game[indexes] = self.COMPUTER_O
        print(f"Ход компьютера: {indexes[0]} {indexes[1]}")
        self.__free_cell_counter -= 1

    def __bool__(self):
        """возвращает True, если игра не окончена и False - в противном случае."""
        return not (self.is_human_win or self.is_computer_win or self.__free_cell_counter == 0)


game = TicTacToe()
game.init()
step_game = 0
for i in game.generate_slices():
    print(i)
game.computer_go()
game.computer_go()
for i in game.generate_slices():
    print(i)
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1

game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")

game.size = 4
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1

game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
