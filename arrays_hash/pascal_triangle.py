# 118, 

from typing import List
class Solution:
    def recursion(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        if numRows == 1:
            return [[1]]
        prevRows = self.recursion(numRows -1)
        newRows = [1] * numRows # array of numbers
        for i in range (1, numRows -1):
            newRows[i] = prevRows[-1][i-1] + prevRows[-1][i]
        
        prevRows.append(newRows)
        return prevRows  

    def dynamic(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        prev_rows = self.generate(numRows - 1)
        prev_row = prev_rows[-1]
        current_row = [1]

        for i in range(1, numRows - 1):
            current_row.append(prev_row[i - 1] + prev_row[i])
        current_row.append(1)

        prev_rows.append(current_row)

        return prev_rows  
    
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for _ in range(numRows - 1):
            dummy_row = [0] + res[-1] + [0]
            row = []

            for i in range(len(res[-1]) + 1): #include the [0] in the dummy row by saying +1
                row.append(dummy_row[i] + dummy_row[i+1])
            res.append(row)
        
        return res

def main():
    s = Solution()
    print(s.generate(5))    
if __name__ == "__main__":
    main()