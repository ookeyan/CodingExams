
def solution(A):
    d = dict()

    unmatched = set()
    for element in A:
        try:
            unmatched.remove(element)
        except KeyError:
            unmatched.add(element)
    return unmatched.pop()