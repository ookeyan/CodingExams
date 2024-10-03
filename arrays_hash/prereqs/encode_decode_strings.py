from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) +"#"+word
        return result

    def decode(self, s: str) -> List[str]:
        res, i = [] , 0
        while i <len(s):
            j = i
            while s[j] != "#":
                j+=1 
            length = int(s[i:j])
            res.append(s[j+1 :j+1+length])
            i =j+1+length

        return res

def main():
    input = ["lint", "code", "love", "you"]
    output =  ["lint", "code", "love", "you"]

    s = Solution()
    val = s.encode(input)
    val1 = s.decode(val)
    print(val1)
if __name__ == "__main__":
    main()