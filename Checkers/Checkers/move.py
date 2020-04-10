import copy
from board import Board
from collections import namedtuple


class Point: # Still unsure of how to use namedtuple so might opt not to use it
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def get_value(self, board):
        return board.grid[self.row][self.col]

    # Define Neighboring points Luke
    def neighbor_points(self):
        # Board values at diagonals of the current point
        pass


class Move:
    def __init__(self, row=None, col=None):
        assert (row, col is not None)
        self.row, self.col = row, col
        self.is_play = (self.row is not None & self.col is not None)

    @classmethod
    def play(cls, row, col):
        return Move(row=row, col=col)


#todo neighbor values  Luke

#todo function that finds if move is within range  Luke

#todo function that finds if move violates rules  Luke



