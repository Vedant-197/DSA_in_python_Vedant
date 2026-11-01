''' Question: Palindrome Partitioning 
    Given a string s, partition s such that every 
    substring of the partition is a palindrome.
'''
def is_palin(s):
    return s == s[::-1]  # Check if string equals its reverse


def solve(s, parts, ans):
    # Base case: string is fully partitioned
    if len(s) == 0:
        ans.append(parts[:])
        return

    # Try cutting the string at every index
    for i in range(len(s)):
        part = s[:i + 1]  # Left part

        if is_palin(part):
            parts.append(part)              # Include part
            solve(s[i + 1:], parts, ans)    # Recurse for right part
            parts.pop()                     # Backtrack



s = input("Enter a string: ")
ans = []
solve(s, [], ans)

print("\nPalindrome Partitions:")
for p in ans:
    print(" | ".join(p))