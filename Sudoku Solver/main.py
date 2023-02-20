from Data import Board

sudoku = Board()
print("Initial Board")

for row in sudoku.board:
    print(row)

print("\n")

sudoku.update()
sudoku.generate_random()
print(sudoku.board)
sudoku.print_blocks()