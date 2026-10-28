def print_board(board):
    for row in board:
        print(*row)


def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False

        if board[i][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        if solve_sudoku(board):
                            return True

                        board[row][col] = 0

                return False

    return True


board = []

print("Enter Sudoku (9 rows, 9 integers per row):")
print("Enter 0 for empty cells.")

for i in range(9):
    row = list(map(int, input().split()))
    board.append(row)

if all(len(row) == 9 for row in board) and all(
    0 <= num <= 9 for row in board for num in row
):
    if solve_sudoku(board):
        print("\nSolved Sudoku:")
        print_board(board)
    else:
        print("No solution exists.")
else:
    print("Invalid input! Enter exactly 9 integers per row, from 0 to 9.")
