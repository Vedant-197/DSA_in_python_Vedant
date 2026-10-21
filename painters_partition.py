'''
Problem Statement:
You are given an array arr of n integers, where arr[i] represents the length of the i-th wooden board. You are also given m painters available to paint these boards.
Each painter takes 1 unit of time to paint 1 unit of a board. Your task is to find the minimum time required to get all the boards painted under the following conditions:

Rules:
1. Contiguous Allocation: A painter can only paint contiguous boards. For example, a painter can paint boards 1 and 2, but cannot paint boards 1 and 3 while skipping 2.
2. Indivisible Boards: A board cannot be split between two painters. A single painter must paint the entire board.
3. Parallel Painting: All available painters can work simultaneously on their assigned boards.

Since all painters work simultaneously, the total time taken to finish the job is equal to the time taken by the \
painter who has the most work. You need to assign the boards to the painters such that this maximum time is as small as possible.

Example :

Input: arr = [40, 30, 10, 20], m = 2

Output: 60

Explanation: We can divide the boards between the 2 painters in the following ways:
Painter 1 gets [40] (Time = 40) and Painter 2 gets [30, 10, 20] (Time = 60). Total time = 60.
Painter 1 gets [40, 30] (Time = 70) and Painter 2 gets [10, 20] (Time = 30). Total time = 70.
Painter 1 gets [40, 30, 10] (Time = 80) and Painter 2 gets [20] (Time = 20). Total time = 80.
The minimum time out of all possible valid allocations is 60.'''\

import numpy as np

def is_possible(arr, n, m, max_allowed_time):
    painters = 1  # Number of painters currently assigned
    time = 0      # Time accumulated by the current painter
    
    for i in range(n):  # Loop variable for iterating through the array
        if time + arr[i] <= max_allowed_time:
            time += arr[i]
        else:
            painters += 1
            time = arr[i]
            
    return painters <= m

def min_time_to_paint(arr, n, m):
    start = np.max(arr)  # Minimum possible max-time limit (lower bound)
    end = np.sum(arr)    # Maximum possible max-time limit (upper bound)
    ans = -1             # Stores the final minimum time required
    
    while start <= end:
        mid = start + (end - start) // 2  # Mid-point of current binary search space
        
        if is_possible(arr, n, m, mid):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
            
    return ans

if __name__ == "__main__":
    # NumPy array inputs constructed from user input string
    arr = np.array(list(map(int, input("Enter board lengths separated by space: ").split()))) 
    n = len(arr)  # Total number of boards
    m = int(input("Enter number of painters: "))  # Total number of available painters from user input
    
    print(f"Minimum time to paint all boards: {min_time_to_paint(arr, n, m)}")