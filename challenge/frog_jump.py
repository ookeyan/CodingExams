def solution(X, Y, D):
    quot, rem = divmod(Y - X, D)
    return quot + 1 if rem != 0 else quot

print(solution(10, 85, 30))
print(solution(0, 10, 1))
print(solution(0, 10, 20))
print(solution(10, 100, 10))
print(solution(10, 10, 10))
print(solution(9, 29, 10))