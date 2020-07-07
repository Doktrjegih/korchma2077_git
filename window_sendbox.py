from tkinter import *
from tkinter import Tk, messagebox
import random


def roll_cubes():
    dice = list()
    for i in range(6):
        buffer = random.randint(1, 6)
        dice.append(buffer)
    print(dice)

root: Tk = Tk()
# Описание параметров окна
root.title("CyberKorchma 2077")
root.geometry('320x240')
root.resizable(False, False)
root.configure(bg="gray")

# кубы внутри окна
cube_1 = Label(root, height=3, width=6, text="1",)
cube_1.grid(row=1, column=1)

cube_2 = Label(root, height=3, width=6, text="2")
cube_2.grid(row=2, column=1)

cube_3 = Label(root, height=3, width=6, text="3")
cube_3.grid(row=3, column=1)

cube_4 = Label(root, height=3, width=6, text="4")
cube_4.grid(row=1, column=3)

cube_5 = Label(root, height=3, width=6, text="5")
cube_5.grid(row=2, column=3)

cube_6 = Label(root, height=3, width=6, text="6")
cube_6.grid(row=3, column=3)

#  тексты внутри окна
global_score = Label(root, text="global score:")
global_score.grid(row=0, column=5)

global_score_count = Label(root, text="00000")
global_score_count.grid(row=0, column=6)

turn_score = Label(root, text="turn score:")
turn_score.grid(row=1, column=5)

turn_score_count = Label(root, text="00000")
turn_score_count.grid(row=1, column=6)

error_bar = Label(root, text="error text")
error_bar.grid(row=0, column=2)

#  кнопки внутри окна
button_roll = Button(root, text="roll it", command=roll_cubes)
button_roll.grid(row=4, column=2)
button_end = Button(root, text="end turn")
button_end.grid(row=4, column=5)

#  Действия внутри окна

root.mainloop()

необходимо научить функцию клик записывать бросок в лейблы кубов.
тогда будет реализован первый бросок визуально, что дост понимание в каком
направлении двигаться дальше.
после нужно будет реализовать счетчик кубов и счетчик очков хода, а так же функцию конца хода.