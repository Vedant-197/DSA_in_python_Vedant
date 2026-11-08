'''finds the Next Smaller Element on the
   left side of each array element.'''

arr = list(map(int, input("Enter array elements: ").split()))
s = []
ans = [0] * len(arr)

for i in range(len(arr)):
    while len(s) > 0 and s[-1] >= arr[i]:
        s.pop()

    if len(s) == 0:
        ans[i] = -1
    else:
        ans[i] = s[-1]

    s.append(arr[i])

print("Next Smaller Elements:", *ans)