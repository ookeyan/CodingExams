from typing import List
#58
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index, len = len(s) -1, 0

        while s[index] == " ":
            index-=1
        while index>=0 and s[index] != " ":
            len +=1
            index -=1

        # len(s.split()[-1])
        return 

def main():
    input = "Hello World  "
    s = Solution()

    print(s.lengthOfLastWord(input))        
if __name__ == "__main__":
    main()