from typing import List
#FIXME

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        pref_len = len(pref)

        for s in strs[1:]:
            while pref != s[0:pref_len]:
                pref_len -= 1
                if pref_len == 0:
                    return ""
                
                pref = pref[0:pref_len]
        
        return pref       

def main():
    strs1 = ["flower","flow","flight"]
    strs2 = ["dog","racecar","car", "dogrcar" ]
    s = Solution()

    print(s.longestCommonPrefix(strs1))
    print(s.longestCommonPrefix(strs2))         
if __name__ == "__main__":
    main()