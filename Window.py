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

        self.board = Board(self, 700, 20)
        self.inputfield = InputField(self)

        master.columnconfigure(1, weight=1)
        master.rowconfigure(0, weight=1)

        master.title("A simple GUI")

    # def __init__(self, master):
    #
    #     self.master = master
    #     self.main = Frame(master= self.master)
    #     self.main.pack()
    #
    #     self.board = Board(self)
    #     self.inputfield = InputField(self)
    #
    #     self.controller = Controller(self)
    #
    #     master.columnconfigure(1, weight=1)
    #     master.rowconfigure(0, weight=1)
    #
    #     master.title("A simple GUI")
    #
    #     # self.label = Label(master, text="This is our first GUI!")
    #     # self.label.pack()
    #     #
    #     # self.greet_button = Button(master, text="Greet", command=self.greet)
    #     # self.greet_button.pack()
    #     #
    #     # self.close_button = Button(master, text="Close", command=master.quit)
    #     # self.close_button.pack()

    def greet(self):
        print("Greetings!")

if __name__ == "__main__":
    root = Tk()
    my_gui = Window(root)
    root.mainloop()