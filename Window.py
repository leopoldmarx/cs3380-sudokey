from tkinter import *

from Board import Board
from Controller import Controller
from InputField import InputField


class Window:

    def __init__(self, master):

        self.master = master
        self.main = Frame(master= self.master)
        self.main.pack()

        self.controller = Controller(self)

        self.dim = 500
        self.pad = 20

        self.board = Board(self, self.dim, self.pad)
        self.inputfield = InputField(self, self.dim, self.pad)

        master.columnconfigure(1, weight=1)
        master.rowconfigure(0, weight=1)

        master.title("A simple GUI")

if __name__ == "__main__":
    root = Tk()
    my_gui = Window(root)
    root.mainloop()