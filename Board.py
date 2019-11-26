from tkinter import Frame

from pip._vendor.msgpack.fallback import xrange

from Cell import Cell

class Board():
    def __init__(self, window):
        self.window  = window
        self.frame = Frame(master=self.window.main)
        self.frame.grid(row=0,column=1)
        self.cells = [[Cell(self, i, j) for i in range(9)] for j in range(9)]

        for cellarray in self.cells:
            for cell in cellarray:
                pass

