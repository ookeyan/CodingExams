from typing import List

#Leetcode 347
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        count = {}
        
        # count the number of times
        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1, 0 ,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return
        
def main():
    nums = [1,1,1,2,2,3]
    k = 2
    s = Solution()
    print(s.topKFrequent(nums, k))
if __name__ == "__main__":
    main()