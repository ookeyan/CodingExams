
from typing import List
#448
# In the first loop, we iterate through the array. For each element, we calculate the
# index it corresponds to in a sorted array of integers. We do this by taking the absolute
# value of the element and subtracting 1 (since arrays are zero-based). If the element is
# positive (not marked as seen), we mark it as negative by negating the value at the 
# calculated index. This step is crucial as it helps us identify which numbers have been
# seen in the array. In the second loop, we iterate through the modified array. 
# This time, we look for indices where the values are still positive. These are the indices
# that correspond to missing numbers in the original array. We push i + 1 (since arrays are
# zero-based) into the result array for each positive value.

class Solution:
  def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

    for i in range(len(nums)):
       idx = abs(nums[i]) - 1
       if nums[idx] > 0:
          nums[idx] *= -1 #mark as seen
    
    res = []

    for i in range(len(nums)):
       if nums[i] > 0:
          res.append(i+1)
    
    return res

    # a = set(nums)
    # b = set(range(1, len(nums)))
    # return list(b.difference(a))

    # for num in nums:
    #   index = abs(num) - 1
    #   nums[index] = -abs(nums[index])

    # return [i + 1 for i, num in enumerate(nums) if num > 0]

def main():
  
  s = Solution()
  print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))

if __name__ == "__main__":
    main()
