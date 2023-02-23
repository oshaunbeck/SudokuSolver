import numpy as np

from .cell import Cell
from typing import List, Optional, Tuple, Set


class Board():
    def __init__(self, values=None):
        self.board_size = (9, 9)
        self.block_size = (3, 3)

        # if values is None:
        #     # Initialize a board with completely empty cells
        #     self.initial_cells = [[Cell(0) for i in range(9)] for i in range(9)]
        # else:
        #     # Initialize a board with the provided values
        #     self.initial_cells = [[Cell(values[i][j]) for j in range(9)] for i in range(9)]
        self.initial_cells = [[Cell(0) for i in range(9)] for i in range(9)]
        self.board = np.asarray(self.initial_cells)

        self.blacklist_update_count = 0
        self.blacklist_zero_count = 0

    # set_num:
    # used to set the cell.num property while simultaneously updating
    # the blacklist of each cell in its corresponding row, col and block.

    def set_num(self, cell: Cell, value: int):

        cell.num = value

        # update blacklists.
        # fill_blacklist will fill all the blacklists of a corresponding cell
        # that is why it must be called each time cell.num is updated.

        self.fill_blacklist(cell)

    def get_unique_candidate(self, cells: List[Cell]) -> Optional[Tuple[Cell, int]]:
        """
        Finds a unique candidate value in a list of cells. If a candidate value is found that is unique to a cell, it is considered
        unique and the corresponding cell is returned along with the candidate value.

        :param cells: a list of cells to check
        :return: a tuple containing the cell and the unique candidate value, or None if no unique candidate is found
        """
        for cell in cells:
            for candidate in cell.candidates:
                unique_candidate = True
                for other_cell in cells:
                    if other_cell != cell and candidate in other_cell.candidates:
                        unique_candidate = False
                        break
                if unique_candidate:
                    return cell, candidate
        return None


    def find_empty_cell(self) -> tuple[int, int]:
        """
        Finds the first empty cell in the board and returns its row and column indices.
        """
        for row in self.board:
            for cell in row:
                if cell == 0:
                    print(f"Found empty cell! ({cell.row}, {cell.col})\n{self.board}")
                    return cell.row, cell.col
        return None

    # BLACKLIST METHODS:
    # These all have the same idea - iterate through the row, column or block
    # that a cell belongs to, find non-zero values in these iterations and add them
    # to the cells blacklist property.

    # fill_blacklist() wll simply call all row, col and block blacklist methods.

    def row_blacklist(self, cell: Cell):

        # Because row_blacklist is called first from fill_blacklist, we will initialise
        # iter_count

        self.blacklist_update_count = 0
        self.blacklist_zero_count = 0

        # Iterate through the row, find any non-zero values and add them to the blacklist.

        for c in self.board[cell.row, :]:
            if c.num == 0:
                self.blacklist_zero_count += 1

            else:
                cell.blacklist.add(c.num)

                self.blacklist_update_count += 1

    def col_blacklist(self, cell: Cell):

        for c in self.board[:, cell.col]:
            if c.num == 0:
                self.blacklist_zero_count += 1
            else:
                cell.blacklist.add(c.num)

                self.blacklist_update_count += 1

    def block_blacklist(self, cell: Cell):

        block = self.blocks[cell.block]

        for c in block.flatten():

            if c == 0:
                self.blacklist_zero_count += 1

            else:
                cell.blacklist.add(c.num)

                self.blacklist_update_count += 1

    def fill_blacklist(self, cell: Cell):

        # print(f"candidates for cell ({cell.position}) before blacklist {cell.candidates}")

        self.row_blacklist(cell)
        self.col_blacklist(cell)
        self.block_blacklist(cell)

        # print(f"candidates for cell ({cell.position}) after {cell.candidates}")

        # print(f"Updated the black list of {self.blacklist_update_count} Cells")
        # print(f"Found {self.blacklist_zero_count} zeros while updating blacklists. total: {self.blacklist_zero_count + self.blacklist_update_count}")

    