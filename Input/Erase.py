import tkinter

from Input.InputNum import InputNum

class Erase(InputNum):
    def __init__(self, inputfield):
        self.inputfield = inputfield

    def click(self):
        self.inputfield.window.board.changeCellVal(0)