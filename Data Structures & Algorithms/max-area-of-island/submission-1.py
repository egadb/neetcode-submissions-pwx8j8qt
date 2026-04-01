class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        mv = [[0,1],[0,-1],[1,0],[-1,0]]

        visited = set()
        maxArea = 0

        def dfs(r, c):
            if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == 0 or (r, c) in visited:
                return 0
            
            visited.add((r,c))
            
            area = 1
            for mr, mc in mv:
               area += dfs(r+mr, c+mc)

            return area



        for r in range(rows):
            for c in range(cols):
                maxArea = max(maxArea, dfs(r, c))

        return maxArea