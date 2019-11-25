from tkinter import Frame

from Input.Erase import Erase
from Input.Num1 import Num1
from Input.Num2 import Num2
from Input.Num3 import Num3
from Input.Num4 import Num4
from Input.Num5 import Num5
from Input.Num6 import Num6
from Input.Num7 import Num7
from Input.Num8 import Num8
from Input.Num9 import Num9
from Undo import Undo


class InputField():
    def __init__(self, window):
        self.window = window
        self.frame = Frame(master=self.window.master).grid(row=4,column=3)
        self.nums = [[Num1(self), Num2(self), Num3(self)],
                     [Num4(self), Num5(self), Num6(self)],
                     [Num7(self), Num8(self), Num9(self)]]
        self.erase = Erase(self)
        self.undo = Undo()
        self.nums = [[Num1(self), Num2(self), Num3(self)],
                     [Num4(self), Num5(self), Num6(self)],
                     [Num7(self), Num8(self), Num9(self)]]
