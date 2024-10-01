from typing import List
#Leetcode 724

class Solution:
    def pivotIndex(self, nums):
        leftSum, rightSum = 0, sum(nums)
        
        for idx, ele in enumerate(nums):
            rightSum -= ele #move closer to the midpoint
            if leftSum == rightSum:
                return idx      # Return the pivot index...
            leftSum += ele #move closer to the midpoint
        return -1     


def main():
    input = [1,7,3,6,5,6]
    input1 =  [1,2,3]
    input2 = [2,1,-1]
    s = Solution()
    print(s.pivotIndex(input))
    print(s.pivotIndex(input1))
    print(s.pivotIndex(input2))

if __name__ == "__main__":
    main()