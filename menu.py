import main as mn


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
    print('About')
    print('[0] Back')
    statement = int(input())
    if statement == 0:
        menu_app()
    else:
        about_app()


def score_app():
    print('High score')
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
        mn.game()


menu_app()
