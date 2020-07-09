one_and_a_half = [1, 2, 3, 4, 5, 6]


def first_combo(list1):
    scores = 0
    a1 = True
    a5 = True

    counter_mass = [0] * 6
    for i in list1:
        count = 0
        for j in range(6):
            count += 1
            if i == count:
                counter_mass[i - 1] += 1

    # проверка на 1500
    if sorted(list1) == one_and_a_half:
        scores += 1500
        a1, a5 = False, False

    # проверка на 3 пары
    if sorted(counter_mass) == [0, 0, 0, 2, 2, 2]:
        scores += 750
        a1, a5 = False, False

    # проверка на 3 и более одинаковых (словарем)
    b1 = dict()
    for i in list1:
        count = 0
        for j in list1:
            if i == j:
                count += 1
                b1[i] = count
    for k in b1:
        if b1[k] == 3 and k != 1 and k != 5:
            scores += k * 100
        elif b1[k] == 4 and k != 1 and k != 5:
            scores += k * 200
        elif b1[k] == 5 and k != 1 and k != 5:
            scores += k * 400
        elif b1[k] == 6 and k != 1 and k != 5:
            scores += k * 800
        elif b1[k] == 3 and k == 1:
            scores += 1000
            a1 = False
        elif b1[k] == 4 and k == 1:
            scores += 2000
            a1 = False
        elif b1[k] == 5 and k == 1:
            scores += 4000
            a1 = False
        elif b1[k] == 6 and k == 1:
            scores += 8000
            a1 = False
        elif b1[k] == 3 and k == 5:
            scores += 500
            a5 = False
        elif b1[k] == 4 and k == 5:
            scores += 1000
            a5 = False
        elif b1[k] == 5 and k == 5:
            scores += 2000
            a5 = False
        elif b1[k] == 6 and k == 5:
            scores += 4000
            a5 = False

    # ебаная проверка КК (а можно бы было втупую сравнить с листом 1-5 или 2-6)
    if sorted(list1) != one_and_a_half:
        ot_1_do_5 = 0
        for i in counter_mass[0:5]:
            if i > 0:
                ot_1_do_5 += 1
        if ot_1_do_5 == 5:
            scores += 500
            a1, a5 = False, False
            if b1[1] == 2:
                scores += 100
            if b1[5] == 2:
                scores += 50
        ot_2_do_6 = 0
        for i in counter_mass[1:6]:
            if i > 0:
                ot_2_do_6 += 1
        if ot_2_do_6 == 5:
            scores += 750
            a1, a5 = False, False
            if b1[5] == 2:
                scores += 50

    # проверка на 1 и 5
    if a1 is True:
        for i in list1:
            if i == 1:
                scores += 100
    if a5 is True:
        for i in list1:
            if i == 5:
                scores += 50

    return scores


def combo(list1):
    scores = 0
    a1 = True
    a5 = True

    def del_cube(cube):
        del (list1[list1.index(cube)])

    counter_mass = [0] * 6
    for i in list1:
        count = 0
        for j in range(6):
            count += 1
            if i == count:
                counter_mass[i - 1] += 1

    # проверка на 1500
    if sorted(list1) == one_and_a_half:
        scores += 1500
        a1, a5 = False, False

    # проверка на 3 пары
    if sorted(counter_mass) == [0, 0, 0, 2, 2, 2]:
        scores += 750
        a1, a5 = False, False

    # проверка на 3 и более одинаковых (словарем)
    b1 = dict()
    for i in list1:
        count = 0
        for j in list1:
            if i == j:
                count += 1
                b1[i] = count
    for k in b1:
        if b1[k] == 3 and k != 1 and k != 5:
            scores += k * 100
        elif b1[k] == 4 and k != 1 and k != 5:
            scores += k * 200
        elif b1[k] == 5 and k != 1 and k != 5:
            scores += k * 400
        elif b1[k] == 6 and k != 1 and k != 5:
            scores += k * 800
        elif b1[k] == 3 and k == 1:
            scores += 1000
            a1 = False
        elif b1[k] == 4 and k == 1:
            scores += 2000
            a1 = False
        elif b1[k] == 5 and k == 1:
            scores += 4000
            a1 = False
        elif b1[k] == 6 and k == 1:
            scores += 8000
            a1 = False
        elif b1[k] == 3 and k == 5:
            scores += 500
            a5 = False
        elif b1[k] == 4 and k == 5:
            scores += 1000
            a5 = False
        elif b1[k] == 5 and k == 5:
            scores += 2000
            a5 = False
        elif b1[k] == 6 and k == 5:
            scores += 4000
            a5 = False

    # ебаная проверка КК (а можно бы было втупую сравнить с листом 1-5 или 2-6)
    if sorted(list1) != one_and_a_half:
        ot_1_do_5 = 0
        for i in counter_mass[0:5]:
            if i > 0:
                ot_1_do_5 += 1
        if ot_1_do_5 == 5:
            scores += 500
            a1, a5 = False, False
            if b1[1] == 2:
                scores += 100
            if b1[5] == 2:
                scores += 50
        ot_2_do_6 = 0
        for i in counter_mass[1:6]:
            if i > 0:
                ot_2_do_6 += 1
        if ot_2_do_6 == 5:
            scores += 750
            a1, a5 = False, False
            if b1[5] == 2:
                scores += 50

    # проверка на 1 и 5
    if a1 is True:
        for i in list1:
            if i == 1:
                scores += 100
                del_cube(i)
    if a5 is True:
        for i in list1:
            if i == 5:
                scores += 50
                del_cube(i)

    print('лист после подсчета комбо: ', list1)
    return scores
