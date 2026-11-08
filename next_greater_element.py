'''find the first greater element on the right side 
of each element, If no then print -1.'''

arr = list(map(int, input("Enter array elements: ").split()))
s = []
ans = [0] * len(arr)

for i in range(len(arr) - 1, -1, -1):

    while len(s) > 0 and s[-1] <= arr[i]:
        s.pop()

    if len(s) == 0:
        ans[i] = -1
    else:
        ans[i] = s[-1]

    s.append(arr[i])

print("Next Greater Elements:", *ans)