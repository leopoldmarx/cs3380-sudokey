import tkinter

from Input.InputNum import InputNum

class Erase(InputNum):
    def __init__(self, inputfield):
        self.val = "Erase"
        self.row = 3
        self.col = 0
        self.inputfield = inputfield
        self.button = tkinter.Button(self.inputfield.frame,
                                     text=self.val,
                                     fg="black",
                                     command=self.click).grid(row=self.row, column=self.col)

    def click(self):
        self.inputfield.window.controller.selected.cellVal.set("")