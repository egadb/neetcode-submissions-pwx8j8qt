'''
run dfs from ocean and find each cell the ocean can receive water from
intersection of set of pacific cells and atlantic cells is the res
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        pacific = set()
        atlantic = set()

        def dfs(r, c, oceanSet):
            oceanSet.add((r,c))

            for dr, dc in directions:
                row, col = r + dr, c + dc
                if row in range(ROWS) and col in range(COLS) and heights[row][col] >= heights[r][c] and (row, col) not in oceanSet:
                    dfs(row, col, oceanSet)


        for c in range(COLS):
            dfs(0, c, pacific)
            dfs(ROWS-1, c, atlantic)

        for r in range(ROWS):
            dfs(r, 0, pacific)
            dfs(r, COLS-1, atlantic)

        return list(pacific.intersection(atlantic))