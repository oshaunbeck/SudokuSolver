from .board import Board

class Cell():

    def __init__(self, num: int, board: Board, position: tuple = (0, 0)):

        self.num = num

        self.position = position

        self.board = board

        self.row = self.position[0]

        self.col = self.position[1]

        self.blacklist = []

    def __repr__(self):

        return f"{self.num}"

    def info(self):

        return f"""
        
        Num:   {self.num}
        Position: {self.position}

        """

    def find_block(self):
        pass

    def check_row(self):

        for idx, row in enumerate(self.board):

            if row[idx] == 0:
                continue
            else:
                self.blacklist.append(row[idx])

    def check_col(self):

        for idx, col in enumerate(self.board.columns):

            if col[idx] == 0:
                continue
            else:
                self.blacklist.append(col[idx])
