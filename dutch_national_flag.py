''' This is more optimise algorithm to sort 0s 1s 2s because it contains only one loop'''

import numpy as np
arr = np.array(list(map(int, input("Enter Elements of an Array: ").split())))

def swap(arr,a,b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def sort(arr):
    n = len(arr)
    low = 0
    mid = 0
    high = n-1

    while (mid <= high):
        if(arr[mid] == 0):
            swap(arr, low, mid)
            low += 1
            mid += 1
        elif(arr[mid] == 1):
            mid += 1
        else:
            swap(arr, high, mid)
            high -= 1

sort(arr)
print(f"Sorted 0s 1s and 2s Array : {arr}")