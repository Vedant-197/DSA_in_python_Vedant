import numpy as np
def bsearch(arr, low, high, target):
    while (low <= high):
        mid = low + (high - low) 

        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

num = int(input("Enter number of elements: "))
arr = np.array(list(map(int, input("Enter the elements of an array: ").split())))

if len(arr) != num:
    print("Error: Please enter exactly", num, "elements.")
else:
    target = int(input("Enter the target element to search: "))

    result = bsearch(arr, 0, len(arr) - 1, target)

    if result != -1:
        print(f"Target element found at index {result}")
    else:
        print("Target element not found")