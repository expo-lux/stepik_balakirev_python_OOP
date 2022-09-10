import curses
import time
import random


class Cell:
    def __init__(self):
        self.is_open = False
        self.is_mine = False
        self.number = 0

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter  # True - в клетке находится мина, False - мина отсутствует
    def is_mine(self, value: bool):
        if type(value) == bool:
            self.__is_mine = value
        else:
            raise ValueError("недопустимое значение атрибута")

    @property  # число мин вокруг клетки
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if type(value) == (int) and 0 <= value <= 8:
            self.__number = value
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_open(self):  # флаг того, открыта клетка или закрыта: True - открыта; False - закрыта.
        return self.__is_open

    @is_open.setter
    def is_open(self, value: bool):
        if type(value) == bool:
            self.__is_open = value
        else:
            raise ValueError("недопустимое значение атрибута")

    def __bool__(self):  # True, если клетка закрыта и False - если открыта.
        return not self.is_open


class GamePole:
    __instance = None  # instance address

    def __new__(cls, *args, **kwargs):  # Singleton implementation
        if cls.__instance:
            return cls.__instance
        else:
            cls.__instance = super().__new__(cls)
            return cls.__instance

    def __init__(self, N, M, total_mines):
        self.__pole_cells = None  # двумерный кортеж NxM объектов Cell
        random.seed(time.time())
        self.__N, self.__M, self.__total_mines = N, M, total_mines  # размер поля N строк x M столбцов
        self.__debug = False
        self.init_pole()

    def valid_coord(self, i, j):
        return 0 <= i <= self.__N - 1 and 0 <= j <= self.__M - 1

    def update_pole(self, row, col):
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if self.valid_coord(i, j) and not self.pole[i][j].is_mine:
                    self.pole[i][j].number += 1

    def show_current_mine_position(self, mines, i, j):
        if self.__debug:
            stdscr.addstr(0, 0, f"Выставляем мину № {mines} на позиции {i} {j}")

    def show_pole(self):
        for i in range(self.__N):
            row = ''
            for j in range(self.__M):
                if self.pole[i][j].is_mine:
                    row += '* '
                elif not self.pole[i][j].is_open:
                    row += '# '
                else:
                    row += str(self.pole[i][j].number) + ' '
            stdscr.addstr(i + 1, 0, row)
        stdscr.refresh()
        time.sleep(0.5)

    def init_pole(self):
        self.__pole_cells = tuple(tuple(Cell() for col in range(self.__M)) for row in range(self.__N))
        mines = 0
        while mines < self.__total_mines:
            rand_row = random.randint(0, self.__N - 1)
            rand_col = random.randint(0, self.__M - 1)
            if self.pole[rand_row][rand_col].is_mine:
                continue
            else:
                self.pole[rand_row][rand_col].is_mine = True
                self.update_pole(rand_row, rand_col)
                mines += 1
            if self.__debug:
                self.show_current_mine_position(mines, rand_row, rand_col)
                self.show_pole()

    @property
    def pole(self):
        return self.__pole_cells

    def open_cell(self, i, j):
        if self.valid_coord(i, j):
            self.__pole_cells[i][j].is_open = True
        else:
            raise IndexError('некорректные индексы i, j клетки игрового поля')


if __name__ == "__main__":

    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()

    try:
        pole = GamePole(20, 60, 60)  # создается поле размерами 10x20 с общим числом мин 10
        pole.init_pole()
        if pole.pole[0][1]:
            pole.open_cell(0, 1)
        if pole.pole[3][5]:
            pole.open_cell(3, 5)
        pole.open_cell(30, 100)  # генерируется исключение IndexError
        pole.show_pole()

    finally:
        curses.echo()
        curses.nocbreak()
        curses.endwin()
