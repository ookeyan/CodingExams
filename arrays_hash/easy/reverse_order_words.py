from typing import List


class Solution:
    def reverse_order_of_words(self, a) -> List[str]:
        return a[::-1]
    
    def reverse_order_of_words1(self, a) -> List[str]:
        result = []
        for i in range(len(a)-1, -1, -1):
            result.append(a[i])
        return result


def main():
    s = Solution()
    a = ["welcome", "to", "pypup"]
    print(s.reverse_order_of_words(a))
    print(s.reverse_order_of_words1(a))
if __name__ == "__main__":
    main()

        