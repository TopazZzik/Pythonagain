# Подключаем логгер
import logging
logging.basicConfig(filename='app.log', encoding='utf-8', level=logging.INFO)

#В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
from datetime import datetime
from sys import argv


def date_validate(date_text: str) -> bool:
    try:
        value = datetime.strptime(date_text, "%d.%m.%Y").date()
        logging.info('Дата правильная!')
        return True
    except:
        logging.warning(f"{date_text} - эта дата содержит ошибку!")
        return False


def _leap_info(date_text: str) -> bool:
    year = int(date_text.split(".")[-1])
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    if (len(argv) < 3):
        logging.error('Нужно ввести дату для проверки!')
        exit()
    else:
        date_validate(argv[2])

#Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
#Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
#Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
#Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
#Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
#Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import random
from copy import copy


class FerziBoard:
    def __init__(self, length: int):
        self.length = length
        self.board = []
        self.all_variants = []
        self._place_next_ferz(0)

    def _can_we_place(self, row: int, num: int):
        for i, value in enumerate(self.board):
            if value == num or (i - row) == (value - num) or (i - row) == (num - value):
                return False
        return True

    def _place_next_ferz(self, row: int):
        if row == self.length:
            self.all_variants.append(copy(self.board))
        else:
            for col in range(self.length):
                if self._can_we_place(row, col):
                    self.board.append(col)
                    self._place_next_ferz(row + 1)
                    self.board.pop()

    def check(self, board: list[int]):
        return board in self.all_variants


def get_random_board(board=[0, 1, 2, 3, 4, 5, 6, 7]):
    random.shuffle(board)
    return board


if __name__ == '__main__':
    length_of_board = 8
    my_boards = FerziBoard(length_of_board)
    print(my_boards.all_variants)
    get_board_from_user = [0] * length_of_board
    for count in range(length_of_board):
        row, col = (int(i) - 1 for i in input(f"Введите пару координат № {count + 1} через пробел: ").split(" "))
        get_board_from_user[col] = row
    print(get_board_from_user)
    print(my_boards.check(get_board_from_user))
    count = 0
    while count < 4:
        random_board = get_random_board()
        if my_boards.check(random_board):
            print(random_board)
            count += 1