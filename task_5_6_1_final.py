from random import randint, choice, seed

seed(1)


class InfFloatValue:
    @classmethod
    def validate(cls, value):
        if not type(value) in (int, float):
            raise ValueError('некорректные координаты и параметры прямоугольника')

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)


class PositiveFloatValue:
    __msg = ''

    def __init__(self, excep_msg="invalid value"):
        if not self.__class__.__msg:
            self.__class__.__msg = excep_msg

    @classmethod
    def validate(cls, value):
        if not (isinstance(value, (float, int)) and value > 0):
            raise ValueError(cls.__msg)

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)


class Rect:
    _width = PositiveFloatValue('некорректные координаты и параметры прямоугольника')
    _height = PositiveFloatValue()
    _x = InfFloatValue()
    _y = InfFloatValue()

    def __init__(self, x, y, width, height):
        self._x, self._y, self._width, self._height = x, y, width, height

    def is_collision(self, rect):
        if self._y > rect._y - rect._height and self._y - self._height < rect._y:
            if self._x < rect._x + rect._width and self._x + self._width > rect._x:
                return True
        return False

    def __repr__(self):
        return f"_x: {self._x} _y: {self._y} _width:{self._width} _height:{self._height}"


class Ship:
    HORIZONTAL = 1
    VERTICAL = 2
    ss = ['', 'hor', 'ver']
    HEALTHY = 1
    DAMAGED = 2

    def __init__(self, length, tp=1, x=None, y=None):
        """_tp - ориентация корабля (1 - горизонтальная; 2 - вертикальная)
        _length - длина корабля (число палуб: целое значение: 1, 2, 3 или 4);
        _сells - состояние палуб, 2 - палуба повреждена, 1 - целая
        _is_move - при попадании в любую палубу устанавливается в False и перемещение корабля по игровому полю прекращается.
        """
        self.set_start_coords(x, y)
        self._length = length
        self._tp = tp
        self._is_move = True
        self._cells = [Ship.HEALTHY] * self._length

    def set_start_coords(self, x, y) -> None:
        """установка начальных координат (запись значений в локальные атрибуты _x, _y)"""
        self._x, self._y = x, y

    def get_start_coords(self) -> tuple:
        """получение начальных координат корабля в виде кортежа x, y"""
        return self._x, self._y

    def move(self, go: int) -> None:
        """перемещение корабля в направлении его ориентации на go клеток (go = 1 - движение в одну сторону на клетку;
         go = -1 - движение в другую сторону на одну клетку); движение возможно только если флаг _is_move = True """
        # print("Двигаем " + str(self) + f" на {go}")
        if self._is_move:
            if self._tp == Ship.HORIZONTAL:
                self._x += go
            elif self._tp == Ship.VERTICAL:
                self._y += go

    def __repr__(self):
        return f"Ship({self._length}, {Ship.ss[self._tp]}, x:{self._x}, y:{self._y})"

    def is_collide(self, ship: 'Ship') -> bool:
        """Проверка на столкновение с другим кораблем ship.
        Возвращает True, если столкновение есть и False - в противном случае """
        if ship == self:
            return False
        if self._tp == Ship.HORIZONTAL:
            Rect1 = Rect(self._x - 1, self._y + 2, self._length + 2, 3)
        elif self._tp == Ship.VERTICAL:
            Rect1 = Rect(self._x - 1, self._y + self._length + 1, 3, self._length + 2)
        if ship._tp == Ship.HORIZONTAL:
            Rect2 = Rect(ship._x, ship._y + 1, ship._length, 1)
        elif ship._tp == Ship.VERTICAL:
            Rect2 = Rect(ship._x, ship._y + ship._length, 1, ship._length)
        return Rect1.is_collision(Rect2)

    def inside(self, size: int) -> bool:
        if self._tp == Ship.HORIZONTAL:
            return 0 <= self._x <= size - self._length and 0 <= self._y <= size - 1
        elif self._tp == Ship.VERTICAL:
            return 0 <= self._x <= size - 1 and 0 <= self._y <= size - self._length

    def is_out_pole(self, size: int) -> bool:
        """Проверка на выход корабля за пределы игрового поля (size - размер игрового поля, обычно, size = 10);
        Возвращает булево значение True, если корабль вышел из игрового поля и False - в противном случае"""
        return not self.inside(size)

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells[key] = value


class GamePole:
    def __init__(self, size=10):
        """size - размер игрового поля"""
        self._size, self._ships = size, []

    def init(self):
        """начальная инициализация игрового поля; здесь создается список из кораблей (объектов класса Ship):
         однопалубных - 4; двухпалубных - 3; трехпалубных - 2; четырехпалубный - 1
         (ориентация этих кораблей должна быть случайной)."""
        # self._ships = [Ship(4, tp=randint(1, 2))]
        self._ships = [Ship(4, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)),
                       Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2))]
        completed_ships, flag_get_next = [], True
        for ship in self._ships:
            while flag_get_next:
                flag_get_next = False
                if ship._tp == ship.VERTICAL:
                    x = randint(0, self._size - 1)
                    y = randint(0, self._size - ship._length)
                elif ship._tp == ship.HORIZONTAL:
                    x = randint(0, self._size - ship._length)
                    y = randint(0, self._size - 1)
                ship.set_start_coords(x, y)
                assert ship.inside(10), "корабль вышел за пределы поля"
                for item in completed_ships:
                    if ship.is_collide(item):
                        flag_get_next = True
                        break
                if not flag_get_next:
                    completed_ships.append(ship)
                    flag_get_next = True
                    break

    def get_ships(self):
        return self._ships

    def move_ships(self):
        """перемещает каждый корабль из коллекции _ships на одну клетку (случайным образом вперед или назад)
         в направлении ориентации корабля; если перемещение в выбранную сторону невозможно
         (другой корабль или пределы игрового поля), то попытаться переместиться в противоположную сторону,
          иначе (если перемещения невозможны), оставаться на месте"""

        def intersects(ship: Ship):
            """Возвращает True если есть пересечения с другими кораблями"""
            for item in self._ships:
                if ship.is_collide(item):
                    return True
            return False

        def invert(step: int):
            return -1 if step == 1 else 1

        for ship in self._ships:
            # step = 1
            step = choice((-1, 1))
            ship.move(step)  # шаг в рандомном направлении
            if not ship.inside(self._size) or intersects(ship):  # если корабль вне поля или есть пересечения
                step = invert(step)  # инвертируем направление
            else:
                # self.show()
                continue
            ship.move(2 * step)  # 2 шага в этом направлении
            if not ship.inside(self._size) or intersects(ship):  # если корабль вне поля или есть пересечения
                step = invert(step)  # инвертируем направление
            else:
                # self.show()
                continue
            ship.move(step)  # возврат на исходную позицию

    def show(self):
        """отображение игрового поля в консоли
                (корабли должны отображаться значениями из коллекции _cells каждого корабля, вода - значением 0);"""
        board = self.get_pole()
        for row in board:
            print()
            for col in row:
                print(col, end=' ')
        print()

    def get_pole(self):
        """получение текущего игрового поля в виде двумерного (вложенного) кортежа размерами size x size элементов"""
        board = [[0 for j in range(self._size)] for i in range(self._size)]
        for ship in self._ships:
            x, y = ship.get_start_coords()
            for cell in ship._cells:
                board[y][x] = cell
                if ship._tp == Ship.VERTICAL:
                    y += 1
                elif ship._tp == Ship.HORIZONTAL:
                    x += 1
        return tuple(tuple(board[y][x] for x in range(self._size)) for y in range(self._size))


ship = Ship(2)
ship = Ship(2, 1)
ship = Ship(3, 2, 0, 0)

assert ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0, "неверные значения атрибутов объекта класса Ship"
assert ship._cells == [1, 1, 1], "неверный список _cells"
assert ship._is_move, "неверное значение атрибута _is_move"

ship.set_start_coords(1, 2)
assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
assert ship.get_start_coords() == (1, 2), "неверно отработал метод get_start_coords()"

ship.move(1)
s1 = Ship(4, 1, 0, 0)
s2 = Ship(3, 2, 0, 0)
s3 = Ship(3, 2, 0, 2)

assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
assert s1.is_collide(
    s3) == False, "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"

s2 = Ship(3, 2, 1, 1)
assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"

s2 = Ship(3, 1, 8, 1)
assert s2.is_out_pole(10), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"

s2 = Ship(3, 2, 1, 5)
assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"

s2[0] = 2
assert s2[0] == 2, "неверно работает обращение ship[indx]"

p = GamePole(10)
p.init()
for nn in range(5):
    for s in p._ships:
        assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"

        for ship in p.get_ships():
            if s != ship:
                assert s.is_collide(ship) == False, "корабли на игровом поле соприкасаются"
    p.move_ships()

gp = p.get_pole()
assert type(gp) == tuple and type(gp[0]) == tuple, "метод get_pole должен возвращать двумерный кортеж"
assert len(gp) == 10 and len(gp[0]) == 10, "неверные размеры игрового поля, которое вернул метод get_pole"

pole_size_8 = GamePole(8)
pole_size_8.init()
print()