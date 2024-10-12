
def gcdOfStrings(str1, str2) -> str:
        # Check if concatenated strings are equal or not, if not return ""
        if str1 + str2 != str2 + str1:
            return ""
        # If strings are equal than return the substring from 0 to gcd of size(str1), size(str2)
        from math import gcd
        return str1[:gcd(len(str1), len(str2))]

def gcdOfStrings1(str1, str2) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) == len(str2):
            return str1
        if len(str1) > len(str2):
            return gcdOfStrings(str1[len(str2):], str2)
        return gcdOfStrings(str1, str2[len(str1):])

str1 = "ABCABC"
str2 = "ABC"
print(gcdOfStrings(str1, str2))
print(gcdOfStrings1(str1, str2))

str1 = "ABABAB"
str2 = "ABAB"
print(gcdOfStrings(str1, str2))
print(gcdOfStrings1(str1, str2))

str1 = "LEET"
str2 = "CODE"
print(gcdOfStrings(str1, str2))
print(gcdOfStrings1(str1, str2))