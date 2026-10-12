import numpy as np

def linears(arr, n, target):
    for i in range(0, n):
        if target == arr[i]:
            return i
    return -1

n = int(input("Enter size of Array: "))
arr = np.array(list(map(int, input("Enter the Elements of an Array: ").split())))

if len(arr)!= n:
    print(f"Error: Please Enter {n} Elements")
else:
    Target = int(input("Enter Target Elements: "))
    result = linears(arr, n, Target)

    if result!= -1:
        print(f"Element Found at index {result}")
    else:
        print("Element is not Found")