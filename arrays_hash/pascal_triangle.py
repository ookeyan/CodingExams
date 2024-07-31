
class Solution:
    def recursion(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        if numRows == 1:
            return [[1]]
        prevRows = self.recursion(numRows -1)
        newRows = [1] * numRows
        for i in range (1, numRows -1):
            newRows[i] = prevRows[-1][i-1] + prevRows[-1[i]]
