# Question: Find all unique combinations in an array that sum up to a target.
# Same number can be used multiple times.

def solve(arr, i, target, ans, comb):
    # Target reached
    if (target == 0):
        if comb not in ans:
            ans.append(comb[:])
        return

    # Invalid case
    if i == len(arr) or target < 0:
        return

    comb.append(arr[i])
    solve(arr, i + 1, target - arr[i], ans, comb)  # Include once
    solve(arr, i, target - arr[i], ans, comb)      # Include multiple times
    comb.pop()                                     # Backtrack

    solve(arr, i + 1, target, ans, comb)           # Exclude


# User inputs
arr = [int(x) for x in input("Enter elements: ").split()]
target = int(input("Enter target: "))

ans = []
solve(arr, 0, target, ans, [])

# Output
if ans:
    print("\nCombinations:")
    for c in ans:
        print(" + ".join(f"{x}" for x in c) + f" = {target}")
else:
    print("\nNo combination (-1)")