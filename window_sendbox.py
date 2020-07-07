from tkinter import *
from tkinter import Tk, messagebox
import random


def roll_cubes():
    dice = list()
    for i in range(6):
        buffer = random.randint(1, 6)
        dice.append(buffer)
    print(dice)
    cube_1.configure(text=dice[0])
    cube_2.configure(text=dice[1])
    cube_3.configure(text=dice[2])
    cube_4.configure(text=dice[3])
    cube_5.configure(text=dice[4])
    cube_6.configure(text=dice[5])

def cube_choice(event):
    messagebox.showinfo("cube", "cube selected")

root: Tk = Tk()
# Описание параметров окна
root.title("CyberKorchma 2077")
root.geometry('320x240')
root.resizable(False, False)

# кубы внутри окна
cube_1 = Label(root, height=3, width=6, text="0",)
cube_1.grid(row=1, column=1)
cube_1.bind("<Button-1>", cube_choice)

cube_2 = Label(root, height=3, width=6, text="0")
cube_2.grid(row=2, column=1)
cube_2.bind("<Button-1>", cube_choice)

cube_3 = Label(root, height=3, width=6, text="0")
cube_3.grid(row=3, column=1)
cube_3.bind("<Button-1>", cube_choice)

cube_4 = Label(root, height=3, width=6, text="0")
cube_4.grid(row=1, column=3)
cube_4.bind("<Button-1>", cube_choice)

cube_5 = Label(root, height=3, width=6, text="0")
cube_5.grid(row=2, column=3)
cube_5.bind("<Button-1>", cube_choice)

cube_6 = Label(root, height=3, width=6, text="0")
cube_6.grid(row=3, column=3)
cube_6.bind("<Button-1>", cube_choice)

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

