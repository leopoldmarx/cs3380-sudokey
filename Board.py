from tkinter import Canvas, BOTH, RIGHT

from math import floor

from Game import Game


class Board():

    def __init__(self, window, dim, margin):
        self.nuteralrowcolor = "lightgrey"
        self.boldrowcolor = "black"
        self.selectedcolor = "red"

        self.originalcolor = "black"
        self.editcolor = "grey"
        self.wrongcolor = "red"

        self.window  = window
        self.margin = margin
        self.dim = dim
        self.side = (dim - margin*2)/9

        self.original = Game.getGame().original
        self.solution = Game.getGame().solution
        self.cells = [[self.original[i][j] for j in range(9)] for i in range(9)]

        self.canvas = Canvas(self.window.main,width=self.dim,
                             height=self.dim)
        self.canvas.pack(fill=BOTH, side=RIGHT)

        self.drawboard()

        self.canvas.bind("<Button-1>", self.setSelected)
        self.window.master.bind("<Key>", self.keyboardInput)

    def drawboard(self):
        self.canvas.delete("all")
        for i in range(10):
            if i % 3 == 0:
                color = self.boldrowcolor
            else:
                color = self.nuteralrowcolor

            self.canvas.create_line(self.margin + i * self.side,
                                    self.margin,
                                    self.margin + i * self.side,
                                    self.dim - self.margin,
                                    fill=color)

            self.canvas.create_line(self.margin,
                                    self.margin + i * self.side,
                                    self.dim - self.margin,
                                    self.margin + i * self.side,
                                    fill=color)

        for i in range(9):
            for j in range(9):
                if self.cells[i][j] != 0:
                    self.writecell(i, j, self.cells[i][j])

        x,y = self.window.controller.selected
        self.selectcell(x,y)

    def changeCellVal(self, val):
        x, y = self.window.controller.selected

        if self.original[x][y] == 0:
            self.cells[x][y] = val
            self.drawboard()

    def writecell(self, x, y, val):
        if self.solution[x][y] != val:
            color = self.wrongcolor
        elif self.original[x][y] == 0:
            color = self.editcolor
        else:
            color = self.originalcolor

        i = self.margin + x * self.side + self.side / 2
        j = self.margin + y * self.side + self.side / 2
        self.canvas.create_text(i, j, text=val, font="Saris 26 bold", tags="numbers", fill=color)

    def setSelected(self, event):

        x, y = event.x, event.y
        if (self.margin < x < self.dim - self.margin and self.margin < y < self.dim - self.margin):
            x, y = floor((x - self.margin) / self.side), floor((y - self.margin) / self.side)
            self.window.controller.selected = x,y
            self.drawboard()

    def keyboardInput(self, event):
        if event.char in "1234567890":
            self.changeCellVal(int(event.char))
        elif event.char == '\x7f':
            self.changeCellVal(0)

    def selectcell(self,x, y):
        self.canvas.create_line(self.margin + x * self.side,
                                self.margin + y * self.side,
                                self.margin + (x + 1) * self.side,
                                self.margin + y * self.side,
                                fill = self.selectedcolor)

        self.canvas.create_line(self.margin + x * self.side,
                                self.margin + (y + 1) * self.side,
                                self.margin + (x + 1) * self.side,
                                self.margin + (y + 1) * self.side,
                                fill=self.selectedcolor)

        self.canvas.create_line(self.margin + x * self.side,
                                self.margin + y * self.side,
                                self.margin + x * self.side,
                                self.margin + (y + 1) * self.side,
                                fill=self.selectedcolor)

        self.canvas.create_line(self.margin + (x + 1) * self.side,
                                self.margin + y * self.side,
                                self.margin + (x + 1) * self.side,
                                self.margin + (y + 1) * self.side,
                                fill=self.selectedcolor)
