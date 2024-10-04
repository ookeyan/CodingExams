
def stairs_count( n : int) -> int :
    one , two = 1 ,1

    for i in range(n-1):
        temp = one
        one = one + two
        two = temp
    return one

print(stairs_count(5))
print(stairs_count(3))
print(stairs_count(2))