from typing import List


def findMin(nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
                
        return nums[left]
    

nums = [3,4,5,1,2]
print(findMin(nums))
nums = [4,5,6,7,0,1,2]
print(findMin(nums))
nums = [11,13,15,17]
print(findMin(nums))