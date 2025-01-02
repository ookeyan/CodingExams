from typing import List


def islandPerimeter(self, grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    perimeter = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                if j - 1 < 0 or grid[i][j-1] == 0: # at the left edge of the board
                    perimeter +=1
                if j + 1 >= cols or grid[i][j+1] == 0: # at the right edge of the board
                    perimeter +=1
                if i - 1 < 0 or grid[i-1][j] == 0: # at the top edge of the board
                    perimeter +=1
                if i + 1 >= rows or grid[i+1][j] == 0: # at the bottom edge of the board
                    perimeter +=1
    
    return perimeter