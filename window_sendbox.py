from tkinter import *
import random
from tkinter import messagebox
from tkinter import Menu


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
    #  что еще происходит при выборе куба?


def cube_remove(event):
    messagebox.showinfo("cube", "cube removed")


root: Tk = Tk()
# Описание параметров окна
root.title("CyberKorchma")
root.geometry('400x240')
root.resizable(False, False)

#  Меню окна
main_menu = Menu(root)
root.config(menu=main_menu)

file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Новая игра")
file_menu.add_command(label="Загрузить")
file_menu.add_command(label="Сохранить")
file_menu.add_command(label="Выход")

help_menu = Menu(main_menu, tearoff=0)
help_menu.add_command(label="Правила")
help_menu.add_command(label="О программе")

main_menu.add_cascade(label="Файл", menu=file_menu)
main_menu.add_cascade(label="Справка", menu=help_menu)

# кубы внутри окна
cube_1 = Label(root, height=3, width=6, text="0", )
cube_1.grid(row=0, column=0)
cube_1.bind("<Button-1>", cube_choice)

cube_2 = Label(root, height=3, width=6, text="0")
cube_2.grid(row=1, column=0)
cube_2.bind("<Button-1>", cube_choice)

cube_3 = Label(root, height=3, width=6, text="0")
cube_3.grid(row=2, column=0)
cube_3.bind("<Button-1>", cube_choice)

cube_4 = Label(root, height=3, width=6, text="0")
cube_4.grid(row=0, column=2)
cube_4.bind("<Button-1>", cube_choice)

cube_5 = Label(root, height=3, width=6, text="0")
cube_5.grid(row=1, column=2)
cube_5.bind("<Button-1>", cube_choice)

cube_6 = Label(root, height=3, width=6, text="0")
cube_6.grid(row=2, column=2)
cube_6.bind("<Button-1>", cube_choice)

#  кубы в буффере
buffer_cube_1 = Label(root, height=3, width=6, text="0", )
buffer_cube_1.grid(row=4, column=0)
buffer_cube_1.bind("<Button-1>", cube_remove)

buffer_cube_2 = Label(root, height=3, width=6, text="0")
buffer_cube_2.grid(row=4, column=1)
buffer_cube_2.bind("<Button-1>", cube_remove)

buffer_cube_3 = Label(root, height=3, width=6, text="0")
buffer_cube_3.grid(row=4, column=2)
buffer_cube_3.bind("<Button-1>", cube_remove)

buffer_cube_4 = Label(root, height=3, width=6, text="0")
buffer_cube_4.grid(row=4, column=3)
buffer_cube_4.bind("<Button-1>", cube_remove)

buffer_cube_5 = Label(root, height=3, width=6, text="0")
buffer_cube_5.grid(row=4, column=4)
buffer_cube_5.bind("<Button-1>", cube_remove)

buffer_cube_6 = Label(root, height=3, width=6, text="0")
buffer_cube_6.grid(row=4, column=5)
buffer_cube_6.bind("<Button-1>", cube_remove)

#  тексты внутри окна
pl1_score = Label(root, text="Player 1 score:")
pl1_score.grid(row=0, column=5)

pl2_score = Label(root, text="Player 2 score:")
pl2_score.grid(row=1, column=5)

pl1_score_count = Label(root, text="00000")
pl1_score_count.grid(row=0, column=6)

pl2_score_count = Label(root, text="00000")
pl2_score_count.grid(row=1, column=6)

turn_score = Label(root, text="turn score:")
turn_score.grid(row=2, column=5)

turn_score_count = Label(root, text="00000")
turn_score_count.grid(row=2, column=6)

#  кнопки внутри окна
button_roll = Button(root, text="roll it", command=roll_cubes)
button_roll.grid(row=3, column=1)
button_end = Button(root, text="end turn")
button_end.grid(row=4, column=6)

#  Действия внутри окна

root.mainloop()
