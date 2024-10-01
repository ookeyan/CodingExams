
#Leetcode 242
from typing import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS , countT = {} , {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) 
            countT[t[i]] = 1 + countT.get(t[i], 0) 

        for letter in countS:
            if countS[letter] != countT.get(letter,0):
                return False 
        return True
    
    def isAnagram1(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

def main():
    s , t = "anagram", "nagaram"
    r , c = "rat" , "car"
    question = Solution()
    print(question.isAnagram(s,t))
    print(question.isAnagram1(r,c))

if __name__ == "__main__":
    main()