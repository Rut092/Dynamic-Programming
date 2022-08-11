class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count=0
        a=len(isConnected)
        vis=[0]*a
        graph=[[] for i in range(a)]

        for i in range(a):
            for j in range(a):
                if i!=j and isConnected[i][j]==1:
                    graph[i].append(j)
                    
        def dfs(n):
            vis[n]=1
            for p in (graph[n]):
                if vis[p]!=1:
                    dfs(p)
                    
        for i in range(a):
            if vis[i]==0:
                count+=1
                dfs(i)
                
        return count