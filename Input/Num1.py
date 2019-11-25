import tkinter

from Input.InputNum import InputNum

class Num1(InputNum):
    def __init__(self, inputfield):
        self.val = 1
        self.row = 0
        self.col = 0
        self.inputfield = inputfield
        self.button = tkinter.Button(self.inputfield.frame,
                                     text=self.val.__str__(),
                                     fg="black",
                                     command=self.click).grid(row=self.row, column=self.col)

    def click(self):
        self.inputfield.window.controller.selected.cellVal.set(self.val)