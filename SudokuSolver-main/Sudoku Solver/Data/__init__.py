from .board import Board
from .cell import Cell
from .board_utils import BoardUtils
from .tests import Tests

sudoku = Board()
test = Tests(sudoku)
util = BoardUtils()

util.str_to_board(sudoku)

print("Inputted Board")

util.update(sudoku)

print(sudoku.board)
util.print_blocks(sudoku)
