
from typing import List

#Leetcode 560
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSums = { 0 : 1 }

        for n in nums:
            curSum += n
            diff = curSum - k 
            res += prefixSums.get(diff, 0)
            prefixSums[curSum]  = prefixSums.get(curSum, 0)
        return res


def main():
    nums = [1,1,1], k = 2
    s = Solution()
    print(s.subarraySum(nums, k))

if __name__ == "__main__":
    main()    
          