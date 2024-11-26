def solution(X, A):
    leaves = set()
    for sec in range (len(A)):
        if A[sec] not in leaves:
            leaves.add(A[sec])
        if len(leaves) == X:
            return True, sec
    return False, -1

print(solution(5, [1,3,1,4,2,3,5,4]))
print(solution(3, [2, 3, 1]))
print(solution(4, [3, 2, 1]))
print(solution(3, [3, 2, 2]))
print(solution(3, [3, 3, 3, 1, 1, 2]))
