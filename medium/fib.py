
class Solution:
    def fib(self, n : int) -> int:
        
        if n == 0:
            return 0    
        if n == 1:
            return 1


        return self.fib(n-1) + self.fib(n-2)


def main():
    s = Solution()
    
    print(s.fib(3))
    print(s.fib(5))

if __name__ == "__main__":
    main()
