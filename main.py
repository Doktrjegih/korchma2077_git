import random
import combo as cb
import menu

test_p = [1, 3, 4, 2, 6, 5]  # used for tests


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
        d1 = list(check())  # откладывание костей
        d2 = list()
        for i in d1:
            d2.append(d[int(i) - 1])
        sc_on_tr, v_c = cb.combo(d2)

        while sorted(d2) != sorted(v_c):
            print('неправильно выбраны кости, попробуйте снова:')
            d1 = list(check())
            d2 = list()
            for i in d1:
                d2.append(d[int(i) - 1])
            sc_on_tr, v_c = cb.combo(d2)

        scr_on_turn = scr_on_turn + sc_on_tr  # подсчет очков за ход /// тут менял cb.combo(d2) на sc_on_tr
        print('лист отложенных костей:', d2, ' подытог хода -', scr_on_turn)
        e = input('кидаем снова? (+/-): ')  # запрос нового броска
        a -= len(d2)  # уменьшение кол-ва кубов в руке
        if e == '-':
            new_high_score(scr_on_turn)
            break
        if e != '+':
            exit()
        if a == 0:
            a = 6
    return scr_on_turn  # возврат функции


def who_goes_first():  # случайный выбор игрока, который ходит первым
    if random.randint(0, 1) == 0:
        return 'Саня'
    else:
        return 'Человек'


def game():
    score1 = 0
    score2 = 0
    limit = int(input('до скольки очков играем\n'))
    turn = who_goes_first()  # первый ход тому, кто выбран в ф-ии who_goes_first
    who = turn
    print(turn + ' ходит первым')
    game_is_playing = True
    while game_is_playing:
        if turn == 'Человек':
            if score2 >= limit:  # проверка на победу второго игрока
                if who == 'Человек':  # проверка на победу по равному кол-ву ходов
                    print('Общие очки Человека =', score1)
                    print('ходов поровну, Саня победил')
                    game_is_playing = False
                else:
                    print('========Последний ход Человека========')
                    a22 = roll()  # роллим и берем результат ф-ии
                    score1 = score1 + a22  # считаем общие очки
                    if score1 > score2:  # проверка на камбэк
                        print('КАМБЭК! Человек победил!')
                        print('Общие очки Человека =', score1)
                        print('Общие очки Сани =', score2)
                        game_is_playing = False
                    elif score1 == score2:  # проверка на ничью
                        print('Общие очки Человека =', score1)
                        print('Общие очки Сани =', score2)
                        print('ничья')
                        game_is_playing = False
                    else:
                        print('Увы, Саня победил')
                        print('Общие очки Сани =', score2)
                        print('Общие очки Человека =', score1)
                        game_is_playing = False
            else:
                print('========Ход Человека========')
                a22 = roll()
                score1 = score1 + a22
                print('Общие очки Человека =', score1)
                if score1 >= limit and who == 'Человек':
                    print('Последний шанс Сани!')
                    turn = 'Саня'
                else:
                    turn = 'Саня'

        if turn == 'Саня':
            if score1 >= limit:
                if who == 'Саня':
                    print('Общие очки Сани =', score2)
                    print('ходов поровну, Человек победил')
                    game_is_playing = False
                else:
                    print('========Последний ход Сани========')
                    b22 = roll()
                    score2 = score2 + b22
                    if score2 > score1:
                        print('КАМБЭК! Саня победил!')
                        print('Общие очки Сани =', score2)
                        print('Общие очки Человека =', score1)
                        game_is_playing = False
                    elif score2 == score1:
                        print('ничья')
                        print('Общие очки Сани =', score2)
                        print('Общие очки Человека =', score1)
                        game_is_playing = False
                    else:
                        print('Увы, Человек победил')
                        print('Общие очки Человека =', score1)
                        print('Общие очки Сани =', score2)
                        game_is_playing = False
            else:
                print('========Ход Сани========')
                b22 = roll()
                score2 = score2 + b22
                print('Общие очки Сани =', score2)
                if score2 >= limit and who == 'Саня':
                    print('Последний шанс Человека!')
                    turn = 'Человек'
                else:
                    turn = 'Человек'
    input('Нажмите любую кнопку для выхода')


def new_high_score(nw_h_scr):
    old = menu.high_score()
    print('старые результаты:', old)
    if nw_h_scr > old[4]:
        name = input('новый рекорд!\nвведите имя: ')
        if nw_h_scr > old[2]:
            if nw_h_scr > old[0]:
                old[5] = old[3]
                old[4] = old[2]
                old[3] = old[1]
                old[2] = old[0]
                old[1] = name
                old[0] = nw_h_scr
            else:
                old[5] = old[3]
                old[4] = old[2]
                old[3] = name
                old[2] = nw_h_scr
        else:
            old[5] = name
            old[4] = nw_h_scr
        w = open('high_score.txt', mode="w", encoding='utf-8')
        for i in old:
            w.write(str(i) + '\n')
        w.close()
        print('новый массив', old)


def check():
    state = True
    while state == True:
        a = input()
        if len(a) > 0 and len(a) < 7:
            for i in a:
                if i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6':
                    continue
                else:
                    if len(a) != 1:
                        duplicate_input = False
                        for j in a:
                            pair = 0
                            for k in a:
                                if j == k:
                                    pair += 1
                            if pair > 1:
                                duplicate_input = True
                        if duplicate_input == False:
                            state = False
                            return a
                    else:
                        state = False
                        return a
