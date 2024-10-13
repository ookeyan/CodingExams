from typing import List

def maxSubArray(nums: List[int]) -> int:
        res = nums[0]
        total = 0

        for n in nums:
            if total < 0:
                total = 0

            total += n
            res = max(res, total)
        
        return res 

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))
nums = [1]
print(maxSubArray(nums))
nums = [5,4,-1,7,8]
print(maxSubArray(nums))