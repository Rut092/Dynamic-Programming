#User function Template for python3

from typing import List

class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        # code here
        n=len(grid)
        m=len(grid[0])
        que=[]
        for i in range(n):
            if grid[i][0]==1:
                que.append([i,0])
                grid[i][0]=0
                
            if grid[i][m-1]==1:
                que.append([i,m-1])
                grid[i][m-1]=0
                
        for i in range(m):
            if grid[0][i]==1:
                que.append([0,i])
                grid[0][i]=0
                
            if grid[n-1][i]==1:
                que.append([n-1,i])
                grid[n-1][i]=0
                
        
        i=0
        while(i<len(que)):
            a,b=que[i]
            i+=1
                
            if a>0 and grid[a-1][b]!=0:
                    que.append([a-1,b])
                    grid[a-1][b]=0
                    
            if a<n-1 and grid[a+1][b]!=0:
                    que.append([a+1,b])
                    grid[a+1][b]=0
                    
            if b>0 and grid[a][b-1]!=0:
                    que.append([a,b-1])
                    grid[a][b-1]=0
                    
            if b<m-1 and grid[a][b+1]!=0:
                    que.append([a,b+1])
                    grid[a][b+1]=0
                    
        
        count=0
        
        for i in range(n):
            for j in range(m):
                count+=grid[i][j]
        
        return count
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int,input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])

        obj=Solution()
        print(obj.numberOfEnclaves(grid))
# } Driver Code Ends