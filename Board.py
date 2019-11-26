from tkinter import Canvas, BOTH, RIGHT

from math import floor

class Board():

    def __init__(self, window, dim, margin):
        self.nuteralcolor = "lightgrey"
        self.boldcolor = "black"
        self.selectedcolor = "red"

        self.window  = window
        self.margin = margin
        self.dim = dim
        self.side = (dim - margin*2)/9

        self.cells = [[0 for i in range(9)] for j in range(9)]

        self.canvas = Canvas(self.window.main,width=self.dim,
                             height=self.dim)
        self.canvas.pack(fill=BOTH, side=RIGHT)

        self.draw_lines()

        self.canvas.bind("<Button-1>", self.setSelected)

    def draw_lines(self):
        for i in range(10):
            if i % 3 == 0:
                color = self.boldcolor
            else:
                color = self.nuteralcolor

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

    def setSelected(self, event):
        # remove highlight of prev cell
        oldx, oldy = self.window.controller.selected
        self.deselectcell(oldx, oldy)

        x, y = event.x, event.y
        if (self.margin < x < self.dim - self.margin and self.margin < y < self.dim - self.margin):
            x, y = floor((x - self.margin) / self.side), floor((y - self.margin) / self.side)
            self.window.controller.selected = x,y
            self.selectcell(x,y)

    def deselectcell(self,x, y):
        self.canvas.create_line(self.margin + x * self.side,
                                self.margin + y * self.side,
                                self.margin + (x + 1) * self.side,
                                self.margin + y * self.side,
                                fill = self.boldcolor if y % 3 == 0 else self.nuteralcolor)

        self.canvas.create_line(self.margin + x * self.side,
                                self.margin + (y + 1) * self.side,
                                self.margin + (x + 1) * self.side,
                                self.margin + (y + 1) * self.side,
                                fill=self.boldcolor if (y + 1) % 3 == 0 else self.nuteralcolor)

        self.canvas.create_line(self.margin + x * self.side,
                                self.margin + y * self.side,
                                self.margin + x * self.side,
                                self.margin + (y + 1) * self.side,
                                fill=self.boldcolor if x % 3 == 0 else self.nuteralcolor)

        self.canvas.create_line(self.margin + (x + 1) * self.side,
                                self.margin + y * self.side,
                                self.margin + (x + 1) * self.side,
                                self.margin + (y + 1) * self.side,
                                fill=self.boldcolor if (x + 1) % 3 == 0 else self.nuteralcolor)

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

    # def __init__(self, window):
    #     self.window  = window
    #     self.frame = Frame(master=self.window.main)
    #     self.frame.grid(row=0,column=1)
    #     self.cells = [[Cell(self, i, j) for i in range(9)] for j in range(9)]
    #
    #     for cellarray in self.cells:
    #         for cell in cellarray:
    #             pass

