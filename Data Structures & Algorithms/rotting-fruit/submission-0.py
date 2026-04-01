class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]] 
        q = deque()

        time = 0
        fresh = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if min(nr,nc) < 0 or nr == rows or nc == cols or grid[nr][nc] != 1:
                        continue

                    grid[nr][nc] = 2
                    q.append((nr,nc))
                    fresh -= 1
                    

            time +=1

        return time if fresh == 0 else -1