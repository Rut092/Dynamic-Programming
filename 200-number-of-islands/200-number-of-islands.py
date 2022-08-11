class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid[0])
        n=len(grid)
        vis=[[0 for i in range(m)] for j in range(n)]
        
        def bfs(i,j):
            vis[i][j]=1
            queue=[[i,j]]
            
            while(len(queue)!=0):
                no=queue.pop(0)
                fst=no[0]
                lst=no[1]
                ind2=lst
                for ind1 in range(fst-1,fst+2):
                    if ind1>=0 and ind1<n and grid[ind1][ind2]=='1' and vis[ind1][ind2]==0:
                        vis[fst][lst]=1
                        queue.append([ind1,ind2])
                ind1=fst
                for ind2 in range(lst-1,lst+2):
                    if ind2>=0 and ind2<m and grid[ind1][ind2]=='1' and vis[ind1][ind2]==0:
                        vis[ind1][ind2]=1
                        queue.append([ind1,ind2])
        
        count=0
        for i in range(n):
            for j in range(m):
                if vis[i][j]==0 and grid[i][j]=='1':
                    count+=1
                    bfs(i,j)
        return count