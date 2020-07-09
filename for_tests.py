import random
import combo as cb


def roll():
    a = 6
    scr_on_turn = 0
    while a > 0:
        d = list()
        for j in range(a):  # бросок костей
            b = random.randint(1, 6)
            d.append(b)
        print('сформирован лист броска - ', d)
        c = cb.combo(d)
        if c == 0:  # проверка, есть ли комбо в броске
            print('нет комбо')
            break
        d2 = list()  # откладывание костей
        print('введите номера костей, которые нужно отложить:')
        d1 = list(input())
        for i in d1:
            if int(i) < 1:
                break
            else:
                d2.append(d[int(i) - 1])
        scr_on_turn = scr_on_turn + cb.combo(d2)
        print('лист отложенных костей:', d2, ' подытог хода -', scr_on_turn)
        e = input('кидаем снова? (Y/N): ')
        if e == 'Y' or e == 'y':
            a -= len(d2)
        if e == 'N' or e == 'n':
            break
