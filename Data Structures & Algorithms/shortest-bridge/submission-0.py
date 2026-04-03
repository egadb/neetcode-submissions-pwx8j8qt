'''
first idea:
find the two islands maybe with two sets (dfs)?
bfs from every starting points on the first island to find shortest path

second idea:
just use bfs two times, once to find the first island, mark with 2s.
second bfs to find the shortest bridge
'''

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        q = deque()

        found = False
        for r in range(ROWS):
            if found: break
            for c in range(COLS):
                print(grid[r][c])
                if grid[r][c] == 1:
                    q.append((r,c))
                    found = True
                    break

        q2 = deque()
        while q:
            r, c = q.popleft()
            grid[r][c] = 2
            q2.append((r,c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1:
                    q.append((nr,nc))

        res = 0
        while q2:
            for _ in range(len(q2)):
                r, c = q2.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc 
                    if nr in range(ROWS) and nc in range(COLS):
                        if grid[nr][nc] == 1:
                            return res
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            q2.append((nr, nc))
            res +=1

        return res