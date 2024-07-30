class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = dict()
        for index, char in enumerate(s):
            if char not in count:
                count[char] = [index, 0]
            else:
                count[char][1] = index

        palindrom_count = 0
        for char in count:
            i, j = count[char]
            if i < j:
                palindrom_count += len(set(s[i+1:j])) #inbetween the left and right
        
        return palindrom_count
    
    def countPalindromicSubsequence2(self, s: str) -> int:
        res = 0
        uniq = set(s) #get all letters
        for char in uniq:
            start = s.find(char)
            end = s.rfind(char)

            if start < end:
                res+= len(set(s[start+1:end]))
        return res

    def practice(self, s: str) -> int:

def main():
    input = "aabca" 
    input2 = "adc"
    input3 = "bbcbaba"
    s = Solution()

    print(s.countPalindromicSubsequence(input))  
    print(s.countPalindromicSubsequence(input2))
    print(s.countPalindromicSubsequence(input3))     
if __name__ == "__main__":
    main()