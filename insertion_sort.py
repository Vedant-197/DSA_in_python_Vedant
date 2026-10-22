import numpy as np

arr = np.array(list(map(int, input("Enter Elements of an Array separated by space: ").split())))
n = len(arr)

def inertion_sort(arr,n):
    for i in range(1,n):
        current = arr[i]
        previous = i-1

        while(previous >=0 and arr[previous]> current):
            arr[previous + 1] = arr[previous]
            previous -= 1

        arr[previous + 1] = current
    return arr

print(f"Sorted Array: {inertion_sort(arr,n)}")