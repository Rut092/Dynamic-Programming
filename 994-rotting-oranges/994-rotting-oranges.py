class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        a=len(grid)
        b=len(grid[0])
        vis=[[0 for i in range(b)] for j in range(a)]
        que=[]
        
        for i in range(a):
            for j in range(b):
                if grid[i][j]==2:
                    que.append([i,j,0])
         
        maxi=0
        while(len(que)!=0):
            i,j,val=que.pop(0)
            maxi=max(maxi,val)
            if i>0:
                if vis[i-1][j]!=2 and grid[i-1][j]==1:
                    grid[i-1][j]=2
                    que.append([i-1,j,val+1])
                    vis[i-1][j]=2
            if j>0:
                if vis[i][j-1]!=2 and grid[i][j-1]==1:
                    grid[i][j-1]=2
                    que.append([i,j-1,val+1])
                    vis[i][j-1]=2
                
            if i<a-1:
                if vis[i+1][j]!=2 and grid[i+1][j]==1:
                    grid[i+1][j]=2
                    que.append([i+1,j,val+1])
                    vis[i+1][j]=2
                    
            if j<b-1:
                if vis[i][j+1]!=2 and grid[i][j+1]==1:
                    grid[i][j+1]=2
                    que.append([i,j+1,val+1])
                    vis[i][j+1]=2
                    
        for i in range(a):
            for j in range(b):
                if grid[i][j]==1:
                    return -1
        return maxi