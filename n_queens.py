def solve_n_queens(n):
    board = [['.' for j in range(n)] for i in range(n)]
    solutions = []

    def is_safe(row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == 'Q':
                return False

        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i][j] == 'Q':
                return False

        return True

    def solve(row):
        if row == n:
            solutions.append(["".join(r) for r in board])
            return

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'  # Place queen
                solve(row + 1)
                board[row][col] = '.'  # Backtrack

    solve(0)
    return solutions


n = int(input("Enter the value of N: "))
ans = solve_n_queens(n)

print("Total Solutions:", len(ans))

for solution in ans:
    for row in solution:
        print(row)
    print()
