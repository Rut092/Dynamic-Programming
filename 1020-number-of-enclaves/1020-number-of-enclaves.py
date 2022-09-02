class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m=len(grid[0])
        n=len(grid)
        
        vis=[[0 for i in range(m)] for i in range(n)]
        
        que=[]
        
        for i in range(n):
            if grid[i][0]==1:
                vis[i][0]=1
                que.append([i,0])
                
            if grid[i][m-1]==1:
                vis[i][m-1]=1
                que.append([i,m-1])
                
        for j in range(0,m):
            if grid[0][j]==1:
                vis[0][j]=1
                que.append([0,j])
                    
            if grid[n-1][j]==1:
                vis[n-1][j]=1
                que.append([n-1,j])
                    
        print(que)
        while(len(que)>0):
            i,j=que.pop(0)

            if i-1>=0 and grid[i-1][j]==1 and vis[i-1][j]==0:
                vis[i-1][j]=1
                que.append([i-1,j])
                
            if i+1<n and grid[i+1][j]==1 and vis[i+1][j]==0:
                vis[i+1][j]=1
                que.append([i+1,j])
                
            if j-1>=0 and grid[i][j-1]==1 and vis[i][j-1]==0:
                vis[i][j-1]=1
                que.append([i,j-1])
                
            if j+1<m and grid[i][j+1]==1 and vis[i][j+1]==0:
                vis[i][j+1]=1
                que.append([i,j+1])
        
        count=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=vis[i][j]:
                    count+=1
        
        return count
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        