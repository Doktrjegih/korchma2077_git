from tkinter import *


def test(event):
    text = ent.get()
    lab['text'] = text


root = Tk()

ent = Entry(root, width=20)
but = Button(root, text="Вывести")
lab = Label(root, width=20, bg='black', fg='white')

but.bind('<Button-1>', test)

ent.pack()
but.pack()
lab.pack()

root.mainloop()
