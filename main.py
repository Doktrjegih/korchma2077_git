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
        scr_on_turn = scr_on_turn + cb.combo(d2)  # подсчет очков за ход
        print('лист отложенных костей:', d2, ' подытог хода -', scr_on_turn)
        e = input('кидаем снова? (+/-): ')  # запрос нового броска
        a -= len(d2)  # уменьшение кол-ва кубов в руке
        if e == '-':
            break
        if a == 0:
            a = 6
    return scr_on_turn  # возврат функции


def who_goes_first():  # случайный выбор игрока, который ходит первым
    if random.randint(0, 1) == 0:
        return 'Саня'
    else:
        return 'Человек'


score1 = 0
score2 = 0
turn = who_goes_first()  # первый ход тому, кто выбран в ф-ии who_goes_first
print('' + turn + ' ходит первым')
gameIsPlaying = True

while gameIsPlaying:

    if turn == 'Человек':
        if score2 > 300:  # проверка на победу второго игрока
            print('========Последний ход Человека========')
            a22 = roll()  # роллим и берем результат ф-ии
            score1 = score1 + a22  # считаем общие очки
            if score1 > score2:  # проверка на камбэк
                print('КАМБЭК! Человек победил!')
                print('Общие очки Человека =', score1)
                print('Общие очки Сани =', score2)
                gameIsPlaying = False
            else:
                print('Увы, Саня победил')
                print('Общие очки Сани =', score2)
                print('Общие очки Человека =', score1)
                gameIsPlaying = False
        else:
            print('========Ход Человека========')
            a22 = roll()
            score1 = score1 + a22
            print('Общие очки Человека =', score1)

            if score1 > 300:
                print('Последний шанс Сани!')
                turn = 'Саня'
            else:
                turn = 'Саня'

    if turn == 'Саня':
        if score1 > 300:
            print('========Последний ход Сани========')
            a22 = roll()
            score1 = score1 + a22
            if score2 > score1:
                print('КАМБЭК! Саня победил!')
                print('Общие очки Сани =', score2)
                print('Общие очки Человека =', score1)
                gameIsPlaying = False
            else:
                print('Увы, Человек победил')
                print('Общие очки Человека =', score1)
                print('Общие очки Сани =', score2)
                gameIsPlaying = False
        else:
            print('========Ход Сани========')
            b22 = roll()
            score2 = score2 + b22
            print('Общие очки Сани =', score2)

            if score1 > 300:
                print('Последний шанс Человека')
                turn = 'Человек'
            else:
                turn = 'Человек'
