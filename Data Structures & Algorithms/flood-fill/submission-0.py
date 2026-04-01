class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
            
        rows, cols = len(image), len(image[0])
        mv = [[-1,0],[1,0],[0,1],[0,-1]]

        def dfs(x,y,c):
            if x > rows-1 or x < 0 or y < 0 or y > cols-1:
                return
            if image[x][y] != c:
                return
            image[x][y] = color

            for mr, mc in mv:
                dfs(x+mr,y+mc,c)


        dfs(sr,sc,image[sr][sc])
        return image