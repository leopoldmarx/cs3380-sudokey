import tkinter

from Input.InputNum import InputNum

class Num(InputNum):
    def __init__(self, inputfield, num):
        self.val = num
        self.inputfield = inputfield

    def click(self):
        self.inputfield.window.board.changeCellVal(self.val)