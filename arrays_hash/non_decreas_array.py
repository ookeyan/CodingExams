from typing import List
# https://leetcode.com/problems/non-decreasing-array/solutions/1190763/js-python-java-c-simple-solution-w-visual-explanation/
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        err = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]: #previous one is bigger
                if err or (i > 1 and i < len(nums)-1 and nums[i-2] > nums[i] and nums[i-1] > nums[i+1]):
                    return False
                err = 1
        return True
    def checkPossibility(self, nums: List[int]) -> bool:
        changed =False 
        for i in range (len(nums)-1):
            if nums[i] <= nums[i+1]:
                continue
            if changed:
                return False
   
            if i==0 or nums[i+1] >= nums[i-1]:
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i]
            changed =True
        return True
def main():
    input = [4,2,1]
    s = Solution()

    print(s.checkPossibility(input))        
if __name__ == "__main__":
    main()