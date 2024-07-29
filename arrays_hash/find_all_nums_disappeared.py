
from typing import List


class Solution:
  def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

    for i in range(len(nums)):
       idx = abs(nums[i]) - 1
       if nums[idx] > 0:
          nums[idx] *= -1
    
    res = []

    for i in range(len(nums)):
       if nums[i] > 0:
          res.append(i+1)
    
    return res

    # a = set(nums)
    # b = set(range(1, len(nums)))
    # return list(b.difference(a))

def main():
  
  s = Solution()
  print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))

if __name__ == "__main__":
    main()
