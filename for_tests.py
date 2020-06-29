from tkinter import *
from tkinter import messagebox


def clicked():
    messagebox.showinfo('Ты пидер', 'Оп, а вот и пидер!')


root = Tk()
root.title("Ты пидер, Санек")
root.geometry('300x300')
lbl = Label(root, text="Санек, ты в курсе, что ты пидер?!", font=("Times New Roman", 12))
lbl.grid(column=0, row=0)
btn = Button(root, text="Тыкни, если пидер", command=clicked)
btn.grid(column=0, row=1)

root.mainloop()


def say_hello(name='test'):
    print("Hello,", name)
