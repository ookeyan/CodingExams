def is_palindrome(s: str) -> bool:
    s = s.lower()
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not alphaNum(s[left]):
            left += 1
        while right > left and not alphaNum(s[right]):
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left , right = left + 1 , right - 1
    
    return True

def alphaNum(c):
    if ( ord("A") <= ord(c) <= ord("Z") or
        ord("a") <= ord(c) <= ord("z") or
        ord("0") <= ord(c) <= ord("9") ):
        return True
    return False


def is_palindrome1(s:str) -> bool:
    newStr = ""
    for c in s:
        if c.isalnum():
            newStr+=c.lower()
    return newStr == newStr[::-1]


# Example usage
print(is_palindrome("Was it a car or a cat I saw?"))  # Output: True
print(is_palindrome("race a car"))                    # Output: False
print(is_palindrome("Mr. Owl ate my metal worm"))
print(is_palindrome("Do geese see God?"))