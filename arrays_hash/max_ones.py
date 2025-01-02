from typing import List

def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    streak = 0
    maximum = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            streak +=1
        else:
            maximum = max(maximum, streak)
            streak = 0
    
    maximum = max(maximum, streak)
    return maximum