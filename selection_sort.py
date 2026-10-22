import numpy as np

arr = np.array(list(map(int, input("Enter Elements of an Array separated by space: ").split())))
n = len(arr)

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def selection_sort_function(arr, n):
    for i in range(0, n - 1):
        small_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[small_index]:
                small_index = j
        swap(arr, i, small_index)
    return arr

print(f"Sorted Array: {selection_sort_function(arr, n)}")