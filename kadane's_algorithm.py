"""Finds the maximum sum of any subarray in the given array.
Returns the maximum sum as an integer."""

import numpy as n
def maxSubArray(nums):
    currSum = 0
    maxSum = -n.inf
    for val in nums:
        currSum += val
        maxSum = n.maximum(currSum, maxSum)
        if currSum < 0:
            currSum = 0
    return int(maxSum)

nums = n.array(list(map(int, input(f"Enter numbers separated by space: ").split())))
print("Maximum subarray sum is:", maxSubArray(nums))