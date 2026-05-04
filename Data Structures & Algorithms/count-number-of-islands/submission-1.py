class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        nbIsland = 0

        def dfs(r, c):
            grid[r][c] = "0"
            for dr, dc in directions:
                row, col = r+dr, c+dc
                if row in range(rows) and col in range(cols) and grid[row][col] == '1':
                    dfs(row, col)
                
            

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    nbIsland += 1

        return nbIsland