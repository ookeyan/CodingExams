

def mergeAlternately(word1: str, word2: str) -> str:

    result = []
    i=0
    
    while i < len(word1) or i < len(word2):
        if i < len(word1):
            result.append(word1[i])
        if i < len(word2):
            result.append(word2[i])
        i += 1
    return ''.join(result)


def mergeAlternately1(word1: str, word2: str) -> str:
    merged = []

    for a, b in zip(word1, word2):
        merged.append(a + b)
    
    merged.append(word1[len(word2):])
    merged.append(word2[len(word1):])

    return "".join(merged)


word1 = "abc"
word2 = "pqr"
word3 = "ab"
word4 = "pqrs"
word5 = "abcd"
word6 = "pq"

print(mergeAlternately1(word1, word2))
print(mergeAlternately1(word3, word4))
print(mergeAlternately1(word5, word6))
print(mergeAlternately(word1, word2))
print(mergeAlternately(word3, word4))
print(mergeAlternately(word5, word6))