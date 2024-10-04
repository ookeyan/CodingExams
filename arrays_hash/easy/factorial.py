
def factorial(n : int) -> int:
    if n == 1:
        return n
    
    return n * factorial(n-1)

def clumsy_factorial(n: int) -> int:
    sign = 1
    ans = 0
    for i in range(n, -1, -4):
        temp = 1
        if i-1 > 0:
            temp *= i-1
        if i-2 > 0:
            temp /= i-2
        ans += sign * temp
        if i-3 > 0:
            temp += i-3       
        sign = -1
    return ans
print(factorial(5))
print(factorial(10))