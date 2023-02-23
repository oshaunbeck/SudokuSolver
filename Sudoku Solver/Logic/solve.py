import numpy as np

from Data import Board

class Solve:
    def __init__(self):

        # How many iterations before the puzzle is solved.
        self.possible_values = {i for i in range(1, 10)}
        self.recursive_counter = 0
        self.hidden_singles_counter = 0
        self.naked_singles_counter = 0
        self.locked_candidates_counter = 0


        self.max_recursions = 100_000
    
    @property
    def total_counter(self):
        return self.recursive_counter + self.naked_singles_counter + self.hidden_singles_counter + self.locked_candidates_counter
    
    def display_counters(self):
        print(f"Number of recursions: {self.recursive_counter}")
        print(f"Number of naked singles: {self.naked_singles_counter}")
        print(f"Number of hidden singles: {self.hidden_singles_counter}")
        print(f"Number of locked candidates found: {self.locked_candidates_counter}")
        print(f"Total iterations: {self.total_counter}")

    def hidden_single(self, board: Board) -> bool:

        """
        Implements the Hidden Single technique: when a row, col or box has a cell with only one candidate, it will be filled.
        """

        
        changed = False

        print("going into hidden_single")

        # candidate_list = [cell.candidates for cell in board.board[empty_cell[0] if cell != 0 or cell is empty_cell]]

        next_empty_pos = board.find_empty_cell()
        empty_cell = board.board[next_empty_pos[0]][next_empty_pos[1]]

        FOUND_STR = f"Hidden Single found!\n{empty_cell.info}"

        # Check row for hidden single

        candidate_list = []

        for cell in board.board[empty_cell.row, :]:

            if cell == 0 and cell is not empty_cell:
                candidate_list.append(cell)

        if board.get_unique_candidate(candidate_list) == None:

            pass

        else:

            cell, val = board.get_unique_candidate(candidate_list)

            board.set_num(cell, val)
            self.hidden_singles_counter += 1

            print(FOUND_STR)
            print(f"Value to update chosen is: {val}")
            changed = True

        # Check cols for hidden single

        candidate_list = []

        for cell in board.board[:, empty_cell.col]:

            

            if cell == 0 and cell is not empty_cell:
                candidate_list.append(cell)

        if board.get_unique_candidate(candidate_list) == None:

            pass

        else:

            cell, val = board.get_unique_candidate(candidate_list)

            board.set_num(cell, val)
            self.hidden_singles_counter += 1

            print(FOUND_STR)
            print(f"Value to update chosen is: {val}")
            changed = True

        # Check blocks for hidden single

        block = board.blocks[empty_cell.block]

        candidate_list = []

        for cell in block.flatten():

            if cell == 0 and cell is not empty_cell:
                candidate_list.append(cell)

        if board.get_unique_candidate(candidate_list) == None:

            pass

        else:

            cell, val = board.get_unique_candidate(candidate_list)

            board.set_num(cell, val)
            self.hidden_singles_counter += 1
            print(FOUND_STR)
            print(f"Value to update chosen is: {val}")
            changed = True


        return changed
                    
    def naked_single(self, board: Board) -> bool:

        """
        Implements the Naked Single technique: when a cell has only one candidate, that candidate must be placed in
        that cell.
        """

        changed = False
        for row in board.board:
            
            board.fill_blacklist(row[0])

            for cell in row:

                if cell.num == 0 and len(cell.candidates) == 1:

                    candidate = list(cell.candidates)[0]

                    board.set_num(cell, candidate)

                    changed = True

                    self.naked_singles_counter +=1
                    
        return changed

    def locked_candidates(self, board: Board) -> bool:
        """
        Implements the Locked Candidates technique: if a candidate value is restricted to one row or column within a
        particular block, then that candidate can be removed from the candidates of all other cells in that row or column.
        """
        changed = False
        
        return changed

    def num_allowed(self, board: Board, row: int, col: int, num: int) -> bool:
        """
        Determines if a given digit can be placed in a given cell without violating any of the rules of Sudoku.
        """

        NOT_ALLOWED_STRING = f"num_allowed did not approve of the number {num} for cell ({row}, {col})"
        # Check if the digit is in the same row or column
        for val in board.board[row, :]:
            if val == num:
                print(NOT_ALLOWED_STRING + "(Same number in row)")
                return False
            
        for val in board.board[:, col]:
            if val == num:
                print(NOT_ALLOWED_STRING + "(Same number in column)")
                return False

        blockID = board.board[row][col].block

        block = board.blocks[blockID]

        for val in block.flatten():
            if val == num:

                print(NOT_ALLOWED_STRING + "(Same number in block)")
                return False
            
        print(f"num {num} is allowed for cell ({row}, {col}) (num_allowed)")
        print(board.board)

        return True
    
    def is_solved(self, board: Board):
        # Check if all cells have a non-zero number
        for row in board.board:
            for cell in row:
                if cell == 0:
                    return False

        # Check each row for duplicates
        for row in range(9):
            if len(set(board.board[row, :])) < 9:
                return False

        # Check each column for duplicates
        for col in range(9):
            if len(set(board.board[:, col])) < 9:
                return False

        # Check each box for duplicates
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = board.board[box_row:box_row+3, box_col:box_col+3].flatten()
                if len(set(box)) < 9:
                    return False

        return True
    def is_valid(self, board: Board) -> bool:
        """
        Checks if the given Sudoku board is valid.
        """

        # Check rows
        for row in board.board:
            row_set = set(cell.num for cell in row if cell.num != 0)
            if len(row_set) != len([cell.num for cell in row if cell.num != 0]):
                return False

        # Check columns
        for col in range(9):
            col_set = set(board.board[row][col].num for row in range(9) if board.board[row][col].num != 0)
            if len(col_set) != len([board.board[row][col].num for row in range(9) if board.board[row][col].num != 0]):
                return False

        # Check blocks
        for block in board.blocks:
            block_set = set(cell.num for cell in block.flatten() if cell.num != 0)
            if len(block_set) != len([cell.num for cell in block.flatten() if cell.num != 0]):
                return False

        return True
    
    def recursive_solve(self, row, col, board: Board):

        self.recursive_counter += 1

        print(f"\nRecursion number: {self.recursive_counter}\n{board.board}")

        if board.find_empty_cell() is None:
            return True

        row, col = board.find_empty_cell()

        while self.naked_single(board) or self.hidden_single(board):
            pass

        if board.board[row][col].num > 0:
            return self.recursive_solve(row, col+1, board)

        print("No naked, hidden Singles currently remaining. No current locked_candidates")
        
        for i in range(1, 10, 1):

            if self.num_allowed(board, row, col, i):

                board.set_num(board.board[row][col], i)
                board.fill_blacklist(board.board[row][col])

                if self.recursive_solve(row, col + 1, board):
                    return True
                
                print("that search failed. backtracking..")

                board.set_num(board.board[row][col], 0)

        if self.recursive_counter > self.max_recursions:
            return True
        
        return False
        

    def solve_board(self, board: Board):
        while True:

            # Attempt to solve recursively
            if self.recursive_solve(0, 0, board):
                break

        print(f"\n\nSolution:\n\n{board.board}")

    

        
        


