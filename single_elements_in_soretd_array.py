''' you are given a sorted array consisting of only integer 
where elements appeare exactly twice except for one which apperars exact once

arr = [1 , 1, 2 ,3 , 3 , 4, 4 , 8 ,8 ]
output is 2
'''
import numpy as np

def single_non_duplicate(A):
    n = len(A)
    st = 0
    end = n - 1
    while st <= end:
        mid = st + (end - st)//2

        if mid == 0:
            if A[0]!= A[1]:
                return A[0]
        elif mid == n - 1:
            if A[n-1]!= A[n-2]:
                return A[n-1]
        else:
            if A[mid-1]!= A[mid] and A[mid]!= A[mid+1]:
                return A[mid]

        if mid % 2 == 0:
            if A[mid-1] == A[mid]:
                end = mid - 1
            else:
                st = mid + 1
        else:
            if A[mid-1] == A[mid]:
                st = mid + 1
            else:
                end = mid - 1
    return -1

n = int(input("Enter size of Array: "))
arr = np.array(list(map(int, input("Enter the Elements of an Array: ").split())))

if len(arr)!= n:
    print(f"Error: Please Enter {n} Elements")
else:
    result = single_non_duplicate(arr)
    print(f"Single Element is {result}")