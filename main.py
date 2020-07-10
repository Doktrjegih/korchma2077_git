#  Code on Python for cube-rolled game "Zonk"

import random
import combo as cb

test_p = [3, 4, 4, 4, 3, 3]  # used for tests


def roll():
    a = 6
    scr_on_turn = 0
    while a > 0:
        d = list()
        for i in range(a):  # бросок костей
            b = random.randint(1, 6)
            d.append(b)
        print('сформирован лист броска - ', d)
        c, v_c = cb.combo(d)  # без второй нельзя, но она нахуй мне не уперлась в этой строке
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
        sc_on_tr, v_c = cb.combo(d2)

        while sorted(d2) != sorted(v_c):
            print('неправильно выбраны кости, попробуйте снова:')
            d1 = list(input())
            d2 = list()
            for i in d1:
                d2.append(d[int(i) - 1])
            sc_on_tr, v_c = cb.combo(d2)

        scr_on_turn = scr_on_turn + sc_on_tr  # подсчет очков за ход /// тут менял cb.combo(d2) на sc_on_tr
        print('лист отложенных костей:', d2, ' подытог хода -', scr_on_turn)
        e = input('кидаем снова? (+/-): ')  # запрос нового броска
        a -= len(d2)  # уменьшение кол-ва кубов в руке
        if e == '-':
            break
        if a == 0:
            a = 6
    return scr_on_turn, v_c  # возврат функции (и че ему тут не нравится?)


def who_goes_first():  # случайный выбор игрока, который ходит первым
    if random.randint(0, 1) == 0:
        return 'Саня'
    else:
        return 'Человек'


score1 = 0
score2 = 0
turn = who_goes_first()  # первый ход тому, кто выбран в ф-ии who_goes_first
who = turn
print('' + turn + ' ходит первым')
gameIsPlaying = True

while gameIsPlaying:

    if turn == 'Человек':
        if score2 >= 3000:  # проверка на победу второго игрока
            if who == 'Человек':  # проверка на победу по равному кол-ву ходов
                print('Общие очки Человека =', score1)
                print('ходов поровну, Саня победил')
                gameIsPlaying = False
            else:
                print('========Последний ход Человека========')
                a22, a32 = roll()  # роллим и берем результат ф-ии
                score1 = score1 + a22  # считаем общие очки
                if score1 > score2:  # проверка на камбэк /// добавить ничью, и снизу тоже
                    print('КАМБЭК! Человек победил!')
                    print('Общие очки Человека =', score1)
                    print('Общие очки Сани =', score2)
                    gameIsPlaying = False
                elif score1 == score2:  # проверка на ничью
                    print('Общие очки Человека =', score1)
                    print('Общие очки Сани =', score2)
                    print('ничья')
                    gameIsPlaying = False
                else:
                    print('Увы, Саня победил')
                    print('Общие очки Сани =', score2)
                    print('Общие очки Человека =', score1)
                    gameIsPlaying = False
        else:
            print('========Ход Человека========')
            a22, a32 = roll()
            score1 = score1 + a22
            print('Общие очки Человека =', score1)
            if score1 >= 3000:
                print('Последний шанс Сани!')
                turn = 'Саня'
            else:
                turn = 'Саня'

    if turn == 'Саня':
        if score1 >= 3000:
            if who == 'Саня':
                print('Общие очки Сани =', score2)
                print('ходов поровну, Человек победил')
                gameIsPlaying = False
            else:
                print('========Последний ход Сани========')
                b22, b32 = roll()
                score2 = score2 + b22
                if score2 > score1:  # добавить ничью
                    print('КАМБЭК! Саня победил!')
                    print('Общие очки Сани =', score2)
                    print('Общие очки Человека =', score1)
                    gameIsPlaying = False
                elif score2 == score1:
                    print('ничья')
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
            b22, b32 = roll()
            score2 = score2 + b22
            print('Общие очки Сани =', score2)
            if score2 >= 3000:
                print('Последний шанс Человека')
                turn = 'Человек'
            else:
                turn = 'Человек'

input('Нажмите любую кнопку для выхода')
exit()