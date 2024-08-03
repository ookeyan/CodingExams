from typing import List
#Leetcode 26
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1 #the first element (index 0) is always unique 
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i] #update and fill the front array
                j += 1
        return j

def main():
    input1 =[0,0,1,1,1,2,2,3,3,4]
    input2 = [1,1,2]
    s = Solution()

    print(s.removeDuplicates(input1))   
    print(s.removeDuplicates(input2))   
if __name__ == "__main__":
    main() 