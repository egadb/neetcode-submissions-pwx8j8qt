class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        nbOfSolutions = 0
        visited = set()
        
        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 1 or (r,c) in visited:
                return 0
            if (r, c) == (rows-1, cols-1):
                return 1

            visited.add((r, c))

            count = 0
            count += dfs(r + 1, c)
            count += dfs(r - 1, c)
            count += dfs(r, c + 1)
            count += dfs(r, c - 1)

            visited.remove((r, c))

            return count



        
        return dfs(0, 0)
