from typing import List
#448
def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing = []
        set_nums = set(nums)
        n = len(nums)

        for val in range(1, n + 1):  # Check all numbers in the range 1 to n
            if val not in set_nums:  # If a number is missing in nums
                missing.append(val)
        return missing    