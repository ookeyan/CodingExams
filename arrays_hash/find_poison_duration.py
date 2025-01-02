from typing import List

def findPoisonedDuration(self, t: List[int], d: int) -> int:
    return d+sum(min(t[i+1]-t[i], d) for i in range(len(t)-1))

def findPoisonedDuration1(self, timeSeries: List[int], duration: int) -> int:
    if not timeSeries:
        return 0
    n = len(timeSeries)
    poisoned_time = 0

    for i in range(n-1):
        # calculate the duration of the poison effect
        duration_of_effect = min(duration, timeSeries[i+1]-timeSeries[i])
        poisoned_time += duration_of_effect
        
    # add the duration of the last poison effect
    poisoned_time += duration

    return poisoned_time

nums = [1,1,0,1,1,1]
print(findPoisonedDuration(nums))
nums = [1,0,1,1,0,1]
print(findPoisonedDuration(nums))
nums = [1,1,0,1,1,1]
print(findPoisonedDuration1(nums))
nums = [1,0,1,1,0,1]
print(findPoisonedDuration1(nums))
 