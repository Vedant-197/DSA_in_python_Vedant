import numpy as np

def search(arr, tar):
    st, end = 0, len(arr)-1
    while st <= end:
        mid = st + (end - st)//2
        if arr[mid] == tar:
            return mid
        if arr[st] <= arr[mid]:
            if arr[st] <= tar <= arr[mid]:
                end = mid-1
            else:
                st = mid+1
        else:
            if arr[mid] <= tar <= arr[end]:
                st = mid+1
            else:
                end = mid-1
    return -1

n = int(input("Enter size of Array: "))
arr = np.array(list(map(int, input("Enter the Elements of an Array: ").split())))

if len(arr)!= n:
    print(f"Error: Please Enter {n} Elements")
else:
    tar = int(input("Enter Target Elements: "))
    result = search(arr, tar)
    if result!= -1:
        print(f"Element Found at index {result}")
    else:
        print("Element is not Found")