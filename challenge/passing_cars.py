MAX_PAIRS = int(1e9)
def solution(A):
    east = passes = 0
    for direction in A:
        if direction == 0:  # Going East.
            east += 1
        else:  # Going West.
            passes += east
        if passes > MAX_PAIRS:  # They do test for this!
            return -1
    return passes