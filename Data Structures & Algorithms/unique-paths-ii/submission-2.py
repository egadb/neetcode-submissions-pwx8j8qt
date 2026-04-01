class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        prevRow = [0]*cols

        for r in range(rows-1,-1,-1):
            currRow = [0]*cols
            if obstacleGrid[r][-1] == 0:
                if r == rows - 1:
                    currRow[-1] = 1
                else:
                    currRow[-1] = prevRow[-1]
            for c in range(cols-2,-1,-1):
                if obstacleGrid[r][c] == 1:
                    currRow[c] = 0
                else:
                    currRow[c] = prevRow[c] + currRow[c+1]
            prevRow = currRow
            
        return prevRow[0]
