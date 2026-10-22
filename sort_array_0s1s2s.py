import numpy as np
arr = np.array(list(map(int, input("Enter Elements of an Array: ").split())))
n = len(arr)
count0 = 0
count1 = 0
count2 = 0

for i in range(0,n):
    if arr[i] == 0:
        count0 += 1
    elif arr[i] == 1:
        count1 += 1
    elif arr[i] == 2:
        count2 += 1

idx = 0
for i in range(0,count0):
    arr[idx] = 0
    idx += 1
for i in range(0,count1):
    arr[idx] = 1
    idx += 1
for i in range(0,count2):
    arr[idx] = 2
    idx += 1

print(f"Sorted 0s 1s and 2s Array: {arr}")