from typing import List
#Leetcode 1929

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * (2 * n)  # Create a new list of size 2n
        for i in range(n):
            result[i] = nums[i]      # Copy to first part
            result[i + n] = nums[i]  # Copy to second part
        return result

    def getConcatenation1(self, nums: List[int]) -> List[int]:
        nums.extend(nums)  # Extend the list with itself
        return nums
    
    def getConcatenation2(self, nums: List[int]) -> List[int]:
        return nums * 2  # Repeat the list twice
def main():
    input1 = [1,2,1] 
    input2 = [1,3,2,1]
    s = Solution()
    print(s.getConcatenation(input1))
    print(s.getConcatenation(input2))
    
if __name__ == "__main__":
    main()
