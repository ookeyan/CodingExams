from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1): #to the left of j
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # No solution found
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []  # No solution found
def main():
    nums , target = [3,4,5,6], 7
    nums1 , target1 = [4,5,6], 10
    nums2 , target2 = [5,5], 10

    s = Solution()
    print(s.twoSum(nums, target))
    print(s.twoSum(nums1, target1))
    print(s.twoSum(nums2, target2))

if __name__ == "__main__":
    main()