heights = list(map(int, input("Enter histogram heights: ").split()))
n = len(heights)

right = [n] * n
left = [-1] * n

s = []

# Next Smaller Right
for i in range(n - 1, -1, -1):
    
    while len(s) > 0 and heights[s[-1]] >= heights[i]:
        s.pop()

    if len(s) == 0:
        right[i] = n
    else:
        right[i] = s[-1]

    s.append(i)

s.clear()

# Next Smaller Left
for i in range(n):

    while len(s) > 0 and heights[s[-1]] >= heights[i]:
        s.pop()

    if len(s) == 0:
        left[i] = -1
    else:
        left[i] = s[-1]

    s.append(i)

# Calculate Maximum Area
ans = 0

for i in range(n):
    height = heights[i]
    width = right[i] - left[i] - 1
    currArea = height * width

    ans = max(ans, currArea)

print("Largest Rectangle Area:", ans)