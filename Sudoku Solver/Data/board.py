import numpy as np

from random import randint

from .cell import Cell


class Board():
    def __init__(self):

        self.board_size = (9, 9)
        self.block_size = (3, 3)

        # Initialize a board with completely empty cells
        self.initial_cells = [[Cell(0) for i in range(9)] for i in range(9)]

        self.board = np.asarray(self.initial_cells)


    def get_columns(self):

        self.columns = [self.board[:, i] for i in range(9)]

    def get_rows(self):

        self.rows = [self.board[i, :] for i in range(9)]

    def print_blocks(self):

        self.block_array = []

        for block in self.blocks:
            self.block_array.append(block)

        print(f"""BLOCKS:
        
{self.block_array[0][0]} {self.block_array[1][0]} {self.block_array[2][0]}
{self.block_array[0][1]} {self.block_array[1][1]} {self.block_array[2][1]}
{self.block_array[0][2]} {self.block_array[1][2]} {self.block_array[2][2]}

{self.block_array[3][0]} {self.block_array[4][0]} {self.block_array[5][0]}
{self.block_array[3][1]} {self.block_array[4][1]} {self.block_array[5][1]}
{self.block_array[3][2]} {self.block_array[4][2]} {self.block_array[5][2]}

{self.block_array[6][0]} {self.block_array[7][0]} {self.block_array[8][0]}
{self.block_array[6][1]} {self.block_array[7][1]} {self.block_array[8][1]}
{self.block_array[6][2]} {self.block_array[7][2]} {self.block_array[8][2]}
        
        """)

    def get_blocks(self):

        self.blocks = np.zeros((9, 3, 3))

        self.blocks = [self.board[i:i+3, j:j+3] for i in range(0, 9, 3) for j in range(0, 9, 3)]

    def update(self):
        
        self.get_rows()
        self.get_columns()
        self.get_blocks()
    
    def generate_random(self):

        print("Generating random")

        for idx, row in enumerate(self.board):

            for pos in range(9):

                row[pos] = Cell(randint(1, 9), (idx, pos))





