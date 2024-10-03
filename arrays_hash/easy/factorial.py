
def factorial(n : int) -> int:
    if n == 1:
        return n
    
    return n * factorial(n-1)

def clumsy_factorial(n: int) -> int:
    for i in range(n, -1, -4):
        temp = 1
        if i-1 > 0:
            temp *= i-1


print(factorial(5))
print(factorial(10))