from tkinter import *

from Board import Board
from Controller import Controller
from InputField import InputField


class Window:
    def __init__(self, master):

        self.master = master
        self.controller = Controller()

        self.inputfieldframe = Frame(master=self.master).grid(row=4,column=3)#.pack(side = "right")

        self.board = Board(self)
        self.inputfield = InputField(self)

        master.title("A simple GUI")

        # self.label = Label(master, text="This is our first GUI!")
        # self.label.pack()
        #
        # self.greet_button = Button(master, text="Greet", command=self.greet)
        # self.greet_button.pack()
        #
        # self.close_button = Button(master, text="Close", command=master.quit)
        # self.close_button.pack()

    def greet(self):
        print("Greetings!")

if __name__ == "__main__":
    root = Tk()
    my_gui = Window(root)
    root.mainloop()