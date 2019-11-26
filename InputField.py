from tkinter import Frame

from Input.Erase import Erase
from Input.Num import Num
from Undo import Undo
import math


class InputField():
    def __init__(self, window):
        self.window = window
        self.frame = Frame(master=self.window.main)
        self.frame.grid(row=0,column=0, sticky="nsw")
        self.nums = [Num(self, i+1, i%3, math.floor(i/3)) for i in range(9)]
        # self.nums = [[Num(self), Num2(self), Num3(self)],
        #              [Num4(self), Num5(self), Num6(self)],
        #              [Num7(self), Num8(self), Num9(self)]]
        self.erase = Erase(self)
        self.undo = Undo(self)
