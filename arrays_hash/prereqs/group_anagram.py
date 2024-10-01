#Leetcode 49
from collections import defaultdict
from typing import  List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs: 
            count = [0] * 26 # index represents the letter
            for char in word:
                count[ord(char) - ord("a")] += 1

            res[tuple(count)].append(word)
        return list(res.values())
    
    def groupAnagrams1(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())

def main():
    s = ["eat","tea","tan","ate","nat","bat"]
    question = Solution()
    print(question.groupAnagrams(s))
    print(question.groupAnagrams1(s))

if __name__ == "__main__":
    main()