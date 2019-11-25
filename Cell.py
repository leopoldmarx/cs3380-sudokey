import tkinter


class Cell():
    def __init__(self, board, x, y):
        self.board = board
        self.cellVal = tkinter.StringVar()
        self.button = tkinter.Button(self.board.frame,
                                     textvariable=self.cellVal,
                                     fg="red",
                                     command=self.setSelected).grid(row = x, column = y)

    def setSelected(self):
        self.board.window.controller.selected = self