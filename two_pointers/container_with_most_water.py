from typing import List

def maxArea(heights: List[int]) -> int:
    l, r = 0, len(heights) - 1
    res = 0

    while l < r:
        area = min(heights[l], heights[r]) * (r - l)
        res = max(res, area)
        if heights[l] <= heights[r]:
            l += 1
        else:
            r -= 1
    return res
    
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
height = [1,1]
print(maxArea(height))