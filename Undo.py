import tkinter


class Undo():
    def __init__(self, inputfield):
        self.val = "Undo"
        self.row = 4
        self.col = 0
        self.inputfield = inputfield
        self.button = tkinter.Button(self.inputfield.frame,
                                     text=self.val,
                                     fg="black",
                                     command=self.click,
                                     borderwidth=30,
                                     relief=tkinter.FLAT).grid(row=self.row, column=self.col, columnspan=3)

    def click(self):
        pass
        #todo