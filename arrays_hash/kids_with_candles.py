from typing import List
def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    m_c = max(candies)
    for i in range(len(candies)):
        if candies[i] + extraCandies >= m_c:
            candies[i] = True
        else:
            candies[i] = False
    return candies

candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))

candies = [4,2,1,1,2]
extraCandies = 1
print(kidsWithCandies(candies, extraCandies))

candies = [12,1,12]
extraCandies = 10
print(kidsWithCandies(candies, extraCandies))