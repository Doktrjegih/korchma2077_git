#  Code on Python for cube-rolled game "Zonk"

import random
import combo as cb

test_p = [1, 2, 4, 6, 3, 3]  # used for tests


def roll():
    a = 6
    scr_on_turn = 0
    while a > 0:
        d = list()
        for i in range(a):  # бросок костей
            b = random.randint(1, 6)
            d.append(b)
        print('сформирован лист броска - ', d)
        c = cb.combo(d)
        if c == 0:  # проверка, есть ли комбо в броске
            print('пока')
            scr_on_turn = 0
            break
        # cb.tips_combo(d)  # подсказки для броска (можно закомментить, если мешает)
        print('введите номера костей, которые нужно отложить:')
        d1 = list(input())  # откладывание костей
        d2 = list()
        for i in d1:
            d2.append(d[int(i) - 1])
        scr_on_turn = scr_on_turn + cb.combo(d2)  # счетчик очков за ход
        print('лист отложенных костей:', d2, ' подытог хода -', scr_on_turn)
        e = input('кидаем снова? (+/-): ')  # запрос нового броска
        a -= len(d2)  # уменьшение кол-ва кубов в руке
        if e == '-':
            break
        if a == 0:
            a = 6
    return scr_on_turn


def whoGoesFirst():
    # Случайный выбор игрока, который ходит первым.
    if random.randint(0, 1) == 0:
        return 'Саня'
    else:
        return 'Человек'


score1 = 0
score2 = 0
turn = whoGoesFirst()
print('' + turn + ' ходит первым')
gameIsPlaying = True

while gameIsPlaying:
    if turn == 'Человек':
        print('========Ход Человека========')
        a22 = roll()
        score1 = score1 + a22
        print('Общие очки Человека =', score1)
        if score1 > 1000:
            print('Человек победил!')
            gameIsPlaying = False
        else:
            turn = 'Саня'
    if turn == 'Саня':
        print('========Ход Сани========')
        b22 = roll()
        score2 = score2 + b22
        print('Общие очки Сани =', score2)
        if score2 > 1000:
            print('Саня победил!')
            gameIsPlaying = False
        else:
            turn = 'Человек'