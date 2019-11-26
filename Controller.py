from Board import Board
from InputField import InputField


class Controller():
    def __init__(self, window):
        self.window = window

        #self.selected = self.window.board.cells[0][0]
        self.selected = 0,0
        #self.selected.button.configure(highlightbackground="lightgrey")