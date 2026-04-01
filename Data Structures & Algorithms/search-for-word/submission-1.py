'''
1. 
kinda like a dfs but you keep in memory the path you took not to retake the same.

start dfs from every position possible

'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r, c, curr):
            if curr == word:
                return True
            elif len(curr) >= len(word):
                return False

            for dr, dc in directions:
                row, col = r + dr, c + dc
                if row in range(ROWS) and col in range(COLS) and (row,col) not in visited:
                    visited.add((row,col))
                    if dfs(row,col,curr+board[row][col]):
                        return True
                    visited.remove((row, col))

            
            return False

        res = False

        for r in range(ROWS):
            for c in range(COLS):
                visited = set()
                visited.add((r,c))
                if dfs(r,c,board[r][c]):
                    return True

        return res