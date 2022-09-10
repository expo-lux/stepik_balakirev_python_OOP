import random


class Cell:
    def __init__(self, around_mines, mine):
        self.around_mines = around_mines  # число мин вокруг клетки (начальное значение 0)
        self.mine = mine  # наличие мины в текущей клетке (True/False)
        self.fl_open = False  # открыта/закрыта клетка - булево значение (True/False)
        pass


class GamePole:
    def __init__(self, N, M):
        random.seed(2)
        self.debug = False
        self.N = N  # размер поля NxN
        self.M = M  # кол-во мин
        self.init()

    def update_pole(self, row, col):
        def valid(num):
            return num >= 0 and num <= self.N - 1

        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if valid(i) and valid(j) and not self.pole[i][j].mine:
                    self.pole[i][j].around_mines += 1

    def init(self):
        self.pole = [[Cell(0, False) for col in range(self.N)] for row in range(self.N)]
        mines = 0
        while mines < self.M:
            rand_row = random.randint(0, self.N - 1)
            rand_col = random.randint(0, self.N - 1)
            if self.debug:
                print(rand_row, rand_col)
            if self.pole[rand_row][rand_col].mine:
                continue
            else:
                self.pole[rand_row][rand_col].mine = True
                self.update_pole(rand_row, rand_col)
                mines += 1
            if self.debug:
                self.show()

    def show(self):
        for i in range(self.N):
            row = ''
            for j in range(self.N):
                if self.pole[i][j].mine:
                    row += '* '
                elif not self.pole[i][j].fl_open:
                    row += '# '
                else:
                    row += str(self.pole[i][j].around_mines) + ' '
            print(row.strip())


pole_game = GamePole(10, 12)
