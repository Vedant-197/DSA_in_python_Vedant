''' Assign c cows to n stalls such that min distance between them is largest possible 
return largest minimum distance'''
import numpy as np

def is_possible(stalls, cows, mid):
    # count
    count = 1
    # last_placed
    last_placed = stalls[0]

    # i
    for i in range(1, len(stalls)):
        # diff
        diff = stalls[i] - last_placed
        if diff >= mid:
            count += 1
            last_placed = stalls[i]
            if count == cows:
                return True
    return False

def aggressive_cows(stalls, cows):
    # stalls
    stalls = np.sort(stalls)
    
    # start
    start = 1
    # end
    end = stalls[-1] - stalls[0]
    # ans
    ans = -1

    while start <= end:
        # mid
        mid = start + (end - start) // 2
        if is_possible(stalls, cows, mid):
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
            
    return ans

if __name__ == "__main__":
    stalls_input = np.array(input("Enter stalls separated by space: ").split(), dtype=int)
    cows_input = np.array(input("Enter number of cows: ").split(), dtype=int)[0]
    
    result = aggressive_cows(stalls_input, cows_input)
    print(f"The largest minimum distance is {result}")