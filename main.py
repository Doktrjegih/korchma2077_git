#  Code on Python for cube-rolled game "Zonk"

import random

# первый бросок
print('введите кол-во костей:')
a = int(input())
d = list()
while a >= 1:
    b = random.randint(1, 6)
    d.append(b)
    a -= 1
print('сформирован лист броска - ', d)

# d = [1, 2, 3, 4, 5, 6]
# print('---отсюда тест---\n', test_p)

# счетчик кубов циклом
counter_mass = [0] * 6
for i in d:
    count = 0
    for j in range(6):
        count += 1
        if i == count:
            counter_mass[i-1] += 1
print('счетчик кубов (сортированный список): ', counter_mass)

# --------------ПРОВЕРКИ КОМБИНАЦИЙ-------------- #

# проверка на 3 и более одинаковых (словарем)
b1 = dict()  # почему нужны скобки?
for i in d:
    count = 0
    for j in d:
        if i == j:
            count += 1
            b1[i] = count
print('счетчик кубов (несортированный словарь): ', b1)
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
for i in d:
    if i == 1 or i == 5:
        print('в кубах есть 1 или 5!')
        break


# проверка на 3 пары
if sorted(counter_mass) == [0, 0, 0, 2, 2, 2]:
    print('три пары: 750 очков и новый бросок')


# проверка на 1500
poltorashka = [1, 2, 3, 4, 5, 6]
if sorted(d) == poltorashka:
    print('полторашка!')

# ебаная проверка КК
# print(counter_mass[0:5], ' - от 1 до 5 должны быть > 0')
# print(counter_mass[1:6], ' - от 2 до 6 должны быть > 0')
ot_1_do_5 = 0
for i in counter_mass[0:5]:
    if i > 0:
        ot_1_do_5 += 1
if ot_1_do_5 == 5:
    print('1-5 комбо, 500 очков!')

ot_2_do_6 = 0
for i in counter_mass[1:6]:
    if i > 0:
        ot_2_do_6 += 1
if ot_2_do_6 == 5:
    print('2-6 комбо, 750 очков!')
#  Антоха смари


123