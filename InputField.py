from tkinter import Frame, BOTH, LEFT

from Input.Erase import Erase
from Input.Num import Num
from Undo import Undo
import math


class InputField():
    def __init__(self, window):
        self.window = window
        self.frame = Frame(master=self.window.main)
        self.frame.pack(fill=BOTH, side=LEFT)
        self.nums = [Num(self, i+1, i%3, math.floor(i/3)) for i in range(9)]
        self.erase = Erase(self)
        self.undo = Undo(self)
