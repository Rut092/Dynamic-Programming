class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        grid=image.copy()
        ini=image[sr][sc]
        a=len(image)
        b=len(image[0])
        vis=[[0 for i in range(b)] for j in range(a)]
        def bfs(x,y):
            if x>=0 and x<a and y>=0 and y<b and vis[x][y]!=1 and image[x][y]==ini:
                grid[x][y]=color
                vis[x][y]=1
                bfs(x-1,y)
                bfs(x+1,y)
                bfs(x,y-1)
                bfs(x,y+1)
            
        bfs(sr,sc)
        return grid