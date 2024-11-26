from typing import List
class Solution:
    def solution(a: List[int], k: int):
        if not len(a):
            return a
        index = 0

        for i in range(k): # move # times
            if index + 1 == len(a): # if at the back go to the front
                index = 0
            else:
                index += 1 # move up 1
        
        dis_from_end = len(a) - index  # our divider
        front_piece = a[:dis_from_end]  # grab the front slice
        back_piece = a[dis_from_end:] # grab the back slice (remaining part)
        return back_piece + front_piece # swap


s = Solution
print(s.solution([3, 8, 9, 7, 6], 3))
print(s.solution([0, 0, 0], 1))
print(s.solution([1, 2, 3, 4], 4))
print(s.solution([6, 3, 8, 9, 7], 0))
print(s.solution([6, 3, 8, 9, 7], 1))
print(s.solution([6, 3, 8, 9, 7], 5))

