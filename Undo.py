import tkinter


class Undo():
    def __init__(self, inputfield):
        self.inputfield = inputfield

    def click(self):
        #prints size of stack
        #self.inputfield.window.board.printStackSize()

        lastIn = self.inputfield.window.board.stack.pop()
        self.inputfield.window.controller.selected = lastIn.x, lastIn.y
        self.inputfield.window.board.UndoCellVal(lastIn.PrevValue)
        #print(lastIn.PrevValue)

