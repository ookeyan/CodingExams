def solution(A):
    collection = set()
    length = 0
    for item in A:
        if item > len(A):
            return 0  # Item is too big for the permutation.
        collection.add(item)
        length += 1
        if len(collection) != length:
            return 0  # Length of set did not increase, so item is a duplicate.
    return 1

def solution2(A):
    new = sorted(A)
    if new[-1] != len(A) or len(set(A)) != len(A):
        return 0
    return 1

