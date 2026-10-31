def get_ans(mat, r, c, path, ans):
    n = len(mat)
    if r < 0 or c < 0 or r >= n or c >= n or mat[r][c] <= 0:
        return
    if r == n - 1 and c == n - 1:          
        ans.append(path)
        return                        
    
    mat[r][c] = -1
    get_ans(mat, r + 1, c, path + "D", ans)
    get_ans(mat, r - 1, c, path + "U", ans)
    get_ans(mat, r, c - 1, path + "L", ans)
    get_ans(mat, r, c + 1, path + "R", ans)
    mat[r][c] = 1                                  # Backtrack


n = int(input("Enter maze size (N): "))
print(f"Enter the {n}x{n} maze row by row:")

maze = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    maze.append(row)

ans = []
get_ans(maze, 0, 0, "", ans)

if ans:
    print("\nPossible paths:")
    for p in ans:
        print(" -> ".join(p))
else:
    print("\nNo path exists (-1)")