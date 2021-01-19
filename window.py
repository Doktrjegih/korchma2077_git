from tkinter import *
import random


def generator():
    for widget in frame.winfo_children():
        widget.destroy()
    for i in range(6):
        i = Cube()


class Cube:
    def __init__(self):
        self.b = str(random.randint(1, 6))
        self.but = Button(frame, text=self.b, command=test)
        self.but.pack(side=LEFT)


root = Tk()
root.geometry('600x400+500+300')
frame = Frame(root)

gen = Button(root, text='Сделать кубы', command=generator)

gen.pack()
frame.pack()

root.mainloop()
