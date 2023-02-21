from Data import Board, Cell


class Check:
    def __init__(self, cell: Cell, board: Board):

        self.cell = cell
        self.board = board
    
    
    # BLACKLIST METHODS:

    # These all have the same intention - iterate through a row, column or block to find
    # and append numbers to a cells blacklist.

    def row_blacklist(self, cell: Cell, board: Board):

        for c in board[cell.row, :]:
            if c.num == 0:
                continue
            else:
                cell.blacklist[c.num] = 1

    def col_blacklist(self, cell: Cell, board: Board):

        for c in board[:, cell.col]:
            if c.num == 0:
                continue
            else:
                cell.blacklist[c.num] = 1

    def block_blacklist(self, cell: Cell, board: Board):

        block = board.blocks[cell.block]

        for c in block:

            if c == 0:
                continue
            else:
                cell.blacklist[c] = 1

    def fill_blacklist(self, cell: Cell, board: Board):

        self.row_blacklist(cell, board)
        self.col_blacklist(cell, board)
        self.block_blacklist(cell, board)