#User function Template for python3

from typing import List

class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        # code here
        que=[[0]+source]
        i=0
        l1,l2=len(grid[0]),len(grid)
        vis=[[0 for i in range(l1)] for j in range(l2)]
        
        if source==destination:
            return 0
            
        while(len(que)>i):
            c,a,b=que[i]
            i+=1
            
            if a>0:
                if grid[a-1][b]==1 and vis[a-1][b]==0:
                    vis[a-1][b]=1
                    if [a-1,b]==destination:
                        return c+1
                    que.append([c+1,a-1,b])
                    
            if b>0:
                if grid[a][b-1]==1 and vis[a][b-1]==0:
                    vis[a][b-1]=1
                    if [a,b-1]==destination:
                        return c+1
                    que.append([c+1,a,b-1])
                    
            if a<l2-1:
                if grid[a+1][b]==1 and vis[a+1][b]==0:
                    vis[a+1][b]=1
                    if [a+1,b]==destination:
                        return c+1
                    que.append([c+1,a+1,b])
                    
            if b<l1-1:
                if grid[a][b+1]==1 and vis[a][b+1]==0:
                    vis[a][b+1]=1
                    if [a,b+1]==destination:
                        return c+1
                    que.append([c+1,a,b+1])
                    
        return -1
        
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

         
if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        source = [0] * 2
        source[0], source[1] = map(int,input().strip().split())
        destination = [0] * 2
        destination[0], destination[1] = map(int,input().strip().split())
        obj=Solution()
        print(obj.shortestPath(grid, source, destination))
# } Driver Code Ends