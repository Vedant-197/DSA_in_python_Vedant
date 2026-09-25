"""Finds the majority element occurring more than n/2 times in the array.
Returns the majority element as an integer."""

def findMajorityElement(arr):
    f = 0
    ans = 0
    for num in arr:
        if f == 0:
            ans = num
        if ans == num:
            f += 1
        else:
            f -= 1
    return ans

arr = list(map(int, input("Enter numbers separated by space: ").split()))
result = findMajorityElement(arr)
print("Majority element is:", result)