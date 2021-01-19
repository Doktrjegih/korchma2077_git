from tkinter import *
import random
import webbrowser


def generator():
    for widget in frame.winfo_children():
        widget.destroy()
    for i in range(6):
        i = Cube()


def help_korchma():
    webbrowser.open('https://github.com/Doktrjegih/korchma2077_git', new=0)


class Cube:
    def __init__(self):
        self.b = str(random.randint(1, 6))
        self.but = Button(frame, text=self.b)
        self.but.pack(side=LEFT)


root = Tk()
root.geometry('600x400+500+300')
mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Новая игра")
filemenu.add_command(label="Лучшие броски")
filemenu.add_command(label="Выход", command=exit)

helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Помощь", command=help_korchma)
helpmenu.add_command(label="О программе")

mainmenu.add_cascade(label="Игра", menu=filemenu)
mainmenu.add_cascade(label="Справка", menu=helpmenu)

frame = Frame(root)

gen = Button(root, text='Кинуть кубы', command=generator)

gen.pack()
frame.pack()
root.mainloop()
