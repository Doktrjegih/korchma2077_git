import tkinter as tk  # импорт библиотеки tkinter


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)


if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title('korchma2077')  # название окна
    root.geometry('650x450+100+100')  # размеры окна + смещение начальной позиции на экране
    root.resizable(False, False)  # изменение размера окна по X и Y
    root.mainloop()
