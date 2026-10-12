import numpy as np

def mountain_idx(arr):
    st = 0
    end = len(arr) - 1
    while st <= end:
        mid = st + (end - st)//2
        if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
            return mid
        elif arr[mid - 1] < arr[mid]:
            st = mid + 1
        else:
            end = mid - 1
    return -1

num = int(input("Enter the Size of an Array: "))
arr = np.array(list(map(int, input("Enter the Elements of an Array: ").split())))
if len(arr)!= num:
    print("Error: Please enter exactly", num, "elements.")
else:
    result = mountain_idx(arr)
    print(f"Mountain Element Found at index {result}")