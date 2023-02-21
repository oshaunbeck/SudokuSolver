import numpy as np

from .cell import Cell


class Board():
    def __init__(self):

        self.board_size = (9, 9)
        self.block_size = (3, 3)

        # Initialize a board with completely empty cells
        self.initial_cells = [[Cell(0) for i in range(9)] for i in range(9)]

        self.board = np.asarray(self.initial_cells)

