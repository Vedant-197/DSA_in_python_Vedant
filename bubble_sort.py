import numpy as np
arr = np.array(list(map(int, input("Enter Elements of an Array seperated by space: ").split())))
n = len(arr)

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def bubble_sort_function(arr, n):
    for i in range(0,n-1):
        for j in range(0,(n - i - 1)):
            if(arr[j] > arr[j+1]):
                swap(arr, j, j+1)
    return arr

print(f"Sorted Array {bubble_sort_function(arr, n)}")