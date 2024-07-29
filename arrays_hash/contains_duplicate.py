from typing import List
 #217
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for n in nums:
            if n in num_set:
                return True
            num_set.add(n)
        return False

def main():
    s = Solution()
if __name__ == "__main__":
    main()