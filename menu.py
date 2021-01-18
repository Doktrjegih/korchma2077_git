import main


def menu_app():
    text = '''Cubes. The Game.
--------------------
Main Menu
--------------------
[1] New Game
[2] High Score
[3] About
[0] Exit
--------------------
*use numerals for select context menu*'''
    print(text)
    statement = int(input())
    if statement == 0:
        exit_app()
    elif statement == 3:
        about_app()
    elif statement == 2:
        score_app()
    elif statement == 1:
        new_game_app()


def exit_app():
    text = '''Cubes. The Game.
--------------------
Exit Game
--------------------
[1] Back
[0] Exit
--------------------
*use numerals for select context menu*'''
    print(text)
    statement = int(input())
    if statement == 0:
        exit()
    elif statement == 1:
        menu_app()


def about_app():
    print('''About
--------------------
Zonk rules

1 = 100
5 = 50
any* х3 = any * 100 (444 = 400)
any* x4(5,6) = any * 100 * 2 (х1,2,3) (55555 = 5 * 100 * 2 х2 = 2000)
*except 1: 111 = 1000, 1111 = 2000, etc.
three pair = 750 and bonus roll
123456 = 1500 and bonus roll
12345 = 500
23456 = 750
''')
    print('[0] Back')
    statement = int(input())
    if statement == 0:
        menu_app()
    else:
        about_app()


def score_app():
    print('High score in 1 roll:')
    a = high_score()
    print(str(a[0]) + ' - ' + str(a[1]))
    print(str(a[2]) + ' - ' + str(a[3]))
    print(str(a[4]) + ' - ' + str(a[5]))
    print('[0] Back')
    statement = int(input())
    if statement == 0:
        menu_app()
    else:
        score_app()


def new_game_app():
    text = '''Cubes. The Game.
--------------------
New Game
--------------------
[1] Start
[0] Back
--------------------
*use numerals for select context menu*'''
    print(text)
    statement = int(input())
    if statement == 0:
        menu_app()
    else:
        main.game()
        menu_app()


def high_score():
    r = open('high_score.txt', mode='r', encoding='utf-8')
    b = []
    for i in r:
        try:
            b.append(int(i.strip()))
        except:
            b.append(i.strip())
    return b


menu_app()
