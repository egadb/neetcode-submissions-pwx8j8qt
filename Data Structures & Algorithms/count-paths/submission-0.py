class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0] * n for _ in range(m)]

        def exploring(r, c):
            if r == m or c == n:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == m - 1 and c == n - 1:
                return 1

            cache[r][c] = exploring(r+1, c) + exploring(r, c+1)
            return cache[r][c]

        return exploring(0,0)