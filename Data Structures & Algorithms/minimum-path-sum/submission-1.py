'''
can there be negative -> no
how big is the array - > 200 x 200

first idea:
make a dfs that kinda searches all the solutions

second idea:
it actually makes sense for this problem to come at it backwards
find minimum at bottom right and build up from there
'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        minGrid = [[float('inf') for i in range(COLS+1)] for j in range(ROWS+1)]

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if r == ROWS-1 and c == COLS-1:
                    minGrid[r][c] = grid[r][c]
                else:
                    minGrid[r][c] = grid[r][c] + min(minGrid[r+1][c], minGrid[r][c+1])
        print(minGrid)
        return minGrid[0][0]