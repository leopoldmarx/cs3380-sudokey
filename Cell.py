import tkinter


class Cell():
    def __init__(self, board, x, y):
        self.board = board
        self.cellVal = tkinter.StringVar()
        self.button = tkinter.Button(self.board.frame,
                                     textvariable=self.cellVal,
                                     fg="black",
                                     command=self.setSelected,
                                     height= 2,
                                     width = 2)
        self.button.grid(row = x, column = y)

    def setSelected(self):
        #remove highlight of prev cell
        self.board.window.controller.selected.button.configure(highlightbackground="white")

        self.button.configure(highlightbackground="lightgrey")
        self.board.window.controller.selected = self
