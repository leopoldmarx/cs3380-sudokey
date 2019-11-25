import tkinter

from Input.InputNum import InputNum

class Num9(InputNum):
    def __init__(self, inputfield):
        self.val = 9
        self.row = 2
        self.col = 2
        self.inputfield = inputfield
        self.button = tkinter.Button(self.inputfield.frame,
                                     text=self.val.__str__(),
                                     fg="black",
                                     command=self.click).grid(row=self.row, column=self.col)

    def click(self):
        self.inputfield.window.controller.selected.cellVal.set(self.val)