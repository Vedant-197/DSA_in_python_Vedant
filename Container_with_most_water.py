"""# We have to calculate maximum watel between walls
You are given an integer array height of length n . There are n
vertical lines drawn such that the two endpoints of the ith line
are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container,
such that the container contains the most water.
return the maximum amount of water a container can store"""

import numpy as n
class Answer_cw:

    def Maxwater(self, heights):
        maxwater = 0
        left = 0
        right = (len(heights) - 1)

        while(left < right):
            width = right - left
            height = min(heights[left], heights[right])
            current_water = width * height
            maxwater = max(current_water, maxwater)

            if(heights[left] < heights[right]):
                left += 1
            else:
                right -= 1

        return maxwater


heights = n.array(list(map(int, input("Enter Heights of wall: ").split())))
mw = Answer_cw()
print(f"Maximum Water Area: {mw.Maxwater(heights)}")