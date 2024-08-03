from typing import List
#Leetcode 217

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for n in nums:
            if n in num_set:
                return True
            num_set.add(n)
        return False
    
    def containsDuplicate1(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

def main():
    input = [1, 2, 3, 3]
    input1 = [1, 2, 3, 4]
    s = Solution()
    print(s.containsDuplicate(input))
    print(s.containsDuplicate1(input))
    print(s.containsDuplicate(input1))
    print(s.containsDuplicate1(input1))
if __name__ == "__main__":
    main()