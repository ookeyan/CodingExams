
def n_partition(n):
   total = 0
   for k in range(1, n + 1): #1-5
       total += helper(n, k)
   return total

def helper(n, k):
   if n <= 0:
       return 0
   if k == 1:
       return 1
   return helper(n - 1, k - 1) + helper(n - k, k)


print(n_partition(5))
print(n_partition(4))