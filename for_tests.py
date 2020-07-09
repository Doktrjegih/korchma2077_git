import random

def roll():
    a = 6
    while a > 0:
        d = list()
        for j in range(a):
            b = random.randint(1, 6)
            d.append(b)
        print('сформирован лист броска - ', d)
        d2 = list()
        print('введите номера костей, которые нужно отложить:')
        d1 = list(input())
        for i in d1:
            if int(i) < 1:
                break
            else:
                d2.append(d[int(i) - 1])
        print('лист отложенных костей:', d2)
        a -= len(d2)
        print(a)


roll()


def say_hello(name='test'):
    print("Hello,", name)
