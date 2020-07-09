#  Code on Python for cube-rolled game "Zonk"

import random
import combo as cb

test_p = [1, 3, 1, 5, 4, 1]  # used for tests

# first roll
d = list()
for i in range(6):
    b = random.randint(1, 6)
    d.append(b)
print('сформирован лист броска - ', test_p)


# проверка на комбо в первом броске
first_roll = cb.first_combo(test_p)
if first_roll == 0:
    print('пока')
    exit(0)
else:
    print(first_roll)


# лист отложенных костей - название для Виталика?)))
d2 = list()
print('введите номера костей, которые нужно отложить:')
d1 = list(input())
for i in d1:
    if int(i) < 1:
        break
    else:
        d2.append(test_p[int(i)-1])
print('лист отложенных костей:', d2)


# проверка отложенного листа
roll = cb.combo(test_p)
if roll == 0:
    print('Нет комбо')
else:
    print(roll)

print(cb.one_and_a_half)