import tkinter as tk


class App:
    window: tk.Tk

    def __init__(self, window: tk.Tk) -> None:
        self.window = window

        self.window.title("Вікно №1")
        self.window.geometry('500x700')
        self.window.resizable(0, 0)
        self.window['bg'] = '#31B404'

    def run(self) -> None:
        self.window.mainloop()


def main():
    App(tk.Tk()).run()


if __name__ == '__main__':
    main()
