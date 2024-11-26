
def solution(N):
    num = str(bin(N)[2:]) 
    
    gap = max_gap = 0
    for char in num:
        if char == "0":
            gap += 1
        else:
            max_gap = max(gap, max_gap)
            gap = 0

    return max_gap 

print(solution(9))
print(solution(529))
print(solution(20))
print(solution(15))
print(solution(32))

