class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1], [1,1], [-1,-1], [1,-1], [-1,1]]

        shortPath = 1
        q = deque()
        if grid[0][0] != 1:
            q.append((0,0))

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == rows - 1 and c == cols - 1:
                    return shortPath

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if min(nr,nc) < 0 or nr == rows or nc == cols or grid[nr][nc] == 1:
                        continue

                    q.append((nr,nc))
                    grid[nr][nc] = 1

            shortPath += 1


        return -1