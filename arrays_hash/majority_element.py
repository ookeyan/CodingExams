from typing import List
#169

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    
        hash = dict()
        major_num = -1
        max = -1

        for n in nums:
            hash[n] = 1+hash.get(n,0)
            if hash[n] > max:
                max = hash[n]
                major_num = n

        # n = len(nums) // 2
        # for key, value in hash.items():
        #     if value > n:
        #         return key
        # return 0
        return major_num
    
    def sorting(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]
   
    def MooreVotingAlgo(self, nums: List[int]) -> int:
        candidate = count =  0
        for n in nums:
            if count == 0:
                candidate = n
            count += 1 if n ==candidate else -1
        return candidate
    
def main():
    input = [2,2,1,1,1,2,2]
    s = Solution()

    print(s.majorityElement(input)) 
    print(s.MooreVotingAlgo(input))        
if __name__ == "__main__":
    main()