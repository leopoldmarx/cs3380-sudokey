from tkinter import Frame

from Cell import Cell

class Board():
    def __init__(self, window):
        self.window  = window
        self.frame = Frame(master=self.window.master).grid(row=9,column=9)
        self.cells = [[Cell(self, i, j) for i in range(9)] for j in range(9)]

        for cellarray in self.cells:
            for cell in cellarray:
                pass

