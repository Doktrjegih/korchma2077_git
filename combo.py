one_and_a_half = [1, 2, 3, 4, 5, 6]


def combo(list1):
    scores = 0
    a1 = True
    a5 = True
    verified_combo = list()  # лист правильного комбо

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
        verified_combo = list1
        a1, a5 = False, False

    # проверка на 3 пары
    if sorted(counter_mass) == [0, 0, 0, 2, 2, 2]:
        scores += 750
        verified_combo = list1
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
            verified_combo.extend([k] * 3)
        elif b1[k] == 4 and k != 1 and k != 5:
            scores += k * 200
            verified_combo.extend([k] * 4)
        elif b1[k] == 5 and k != 1 and k != 5:
            scores += k * 400
            verified_combo.extend([k] * 5)
        elif b1[k] == 6 and k != 1 and k != 5:
            scores += k * 800
            verified_combo.extend([k] * 6)
        elif b1[k] == 3 and k == 1:
            scores += 1000
            verified_combo.extend([k] * 3)
            a1 = False
        elif b1[k] == 4 and k == 1:
            scores += 2000
            verified_combo.extend([k] * 4)
            a1 = False
        elif b1[k] == 5 and k == 1:
            scores += 4000
            verified_combo.extend([k] * 5)
            a1 = False
        elif b1[k] == 6 and k == 1:
            scores += 8000
            verified_combo.extend([k] * 6)
            a1 = False
        elif b1[k] == 3 and k == 5:
            scores += 500
            verified_combo.extend([k] * 3)
            a5 = False
        elif b1[k] == 4 and k == 5:
            scores += 1000
            verified_combo.extend([k] * 4)
            a5 = False
        elif b1[k] == 5 and k == 5:
            scores += 2000
            verified_combo.extend([k] * 5)
            a5 = False
        elif b1[k] == 6 and k == 5:
            scores += 4000
            verified_combo.extend([k] * 6)
            a5 = False

    # ебаная проверка КК (а можно бы было втупую сравнить с листом 1-5 или 2-6)
    if sorted(list1) != one_and_a_half:
        from_1_to_5 = 0
        for i in counter_mass[0:5]:
            if i > 0:
                from_1_to_5 += 1
        if from_1_to_5 == 5:
            scores += 500
            verified_combo.extend([1, 2, 3, 4, 5])
            a1, a5 = False, False
            if b1[1] == 2:
                scores += 100
                verified_combo.append(1)
            if b1[5] == 2:
                scores += 50
                verified_combo.append(5)
        from_2_to_6 = 0
        for i in counter_mass[1:6]:
            if i > 0:
                from_2_to_6 += 1
        if from_2_to_6 == 5:
            scores += 750
            verified_combo.extend([2, 3, 4, 5, 6])
            a1, a5 = False, False
            if b1[5] == 2:
                scores += 50
                verified_combo.append(5)

    # проверка на 1 и 5
    if a1 is True:
        for i in list1:
            if i == 1:
                scores += 100
                verified_combo.append(1)
    if a5 is True:
        for i in list1:
            if i == 5:
                scores += 50
                verified_combo.append(5)

    return scores, verified_combo


def tips_combo(list1):  # ПРОВЕРКИ КОМБИНАЦИЙ (без счета)
    # счетчик кубов циклом
    counter_mass = [0] * 6
    for i in list1:
        count = 0
        for j in range(6):
            count += 1
            if i == count:
                counter_mass[i - 1] += 1
    # print('счетчик кубов (сортированный список): ', counter_mass)

    # проверка на 3 и более одинаковых (словарем)
    b1 = dict()
    for i in list1:
        count = 0
        for j in list1:
            if i == j:
                count += 1
                b1[i] = count
    # print('счетчик кубов (несортированный словарь): ', b1)
    for k in b1:
        if b1[k] == 3:
            print('троечька')
        elif b1[k] == 4:
            print('четыре, неплохо')
        elif b1[k] == 5:
            print('пятерка, воу!')
        elif b1[k] == 6:
            print('ДЖЕКПОТ!!!')

    # проверка на 1 и 5
    for i in list1:
        if i == 1 or i == 5:
            print('в кубах есть 1 или 5!')
            break

    # проверка на 3 пары
    if sorted(counter_mass) == [0, 0, 0, 2, 2, 2]:
        print('три пары: 750 очков и новый бросок')

    # проверка на 1500
    if sorted(list1) == one_and_a_half:
        print('полторашка!')

    # ебаная проверка КК
    # print(counter_mass[0:5], ' - от 1 до 5 должны быть > 0')
    # print(counter_mass[1:6], ' - от 2 до 6 должны быть > 0')
    from_1_to_5 = 0
    for i in counter_mass[0:5]:
        if i > 0:
            from_1_to_5 += 1
    if from_1_to_5 == 5:
        print('1-5 комбо, 500 очков!')

    from_2_to_6 = 0
    for i in counter_mass[1:6]:
        if i > 0:
            from_2_to_6 += 1
    if from_2_to_6 == 5:
        print('2-6 комбо, 750 очков!')
