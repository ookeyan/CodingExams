def solution(A):
    full_array = range(1, len(A) + 2)
    return sum(full_array) - sum(A)