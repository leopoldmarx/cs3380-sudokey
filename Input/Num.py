import tkinter

from Input.InputNum import InputNum

class Num(InputNum):
    def __init__(self, inputfield, num, row, col):
        self.val = num
        self.inputfield = inputfield
        self.button = tkinter.Button(self.inputfield.frame,
                                     text=self.val.__str__(),
                                     fg="black",
                                     command=self.click).grid(row=row, column=col)

    def click(self):
        self.inputfield.window.controller.selected.cellVal.set(self.val)