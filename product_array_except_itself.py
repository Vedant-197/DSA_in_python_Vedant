''' Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums [i] .
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in 0(n) time and without using the division
operation  

ex - if we have some array like [4 ,3 ,5 ,6] so it will return product of an array excepts self index 
      an array is [90, 120, 72, 60]    i.e actual logic is going like this->
        [(3*5*6),(4*5*6),(4*3*6),(4*3*5)]'''

import numpy as np
arr = np.array(list(map(int,input("Entre Elements of an Array: ").split())))
ans = np.ones(len(arr),dtype=int)

for i in  range(1,len(arr)):
    ans[i] = ans[i-1] * arr[i-1]

suffix = 1
for i in  range((len(arr)-2), -1, -1):
    suffix *= arr[i+1]
    ans[i] *= suffix

print(f"Result Array: {ans}")


