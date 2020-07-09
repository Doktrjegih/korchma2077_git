#  Code on Python for cube-rolled game "Zonk"

import random
import combo as cb

test_p = [1, 3, 1, 5, 4, 1]  # used for tests


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
            print('нет комбо')
            break
        cb.tips_combo(d)  # подсказки для броска (можно закомментить, если мешает)
        d2 = list()  # откладывание костей
        print('введите номера костей, которые нужно отложить:')
        d1 = list(input())
        for i in d1:
            if int(i) < 1:
                break
            else:
                d2.append(d[int(i) - 1])
        scr_on_turn = scr_on_turn + cb.combo(d2)  # счетчик очков за ход
        print('лист отложенных костей:', d2, ' подытог хода -', scr_on_turn)
        e = input('кидаем снова? (+/-): ')  # запрос нового броска
        a -= len(d2)
        if e == '-':
            break
        if a == 0:
            a = 6


roll()
