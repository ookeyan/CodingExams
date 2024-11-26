from typing import List
def solution(A: List[int]): 
    min_sum = 999

    for i in range(1, len(A)-1):

        a = sum(A[:i])
        b = sum(A[i:])
        diff = abs(a-b)
        if min_sum > diff:
            min_sum = diff  
    return min_sum

print(solution([3,1,2,4,3]))