class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        vis=[-1 for i in range(V)]
        self.stack=[]
        for i in range(V):
            if vis[i]==-1:
                vis[i]=1
                self.dfs(i,v,adj,vis)
                self.stack.append(i)
        return self.stack[::-1]
                
    def dfs(self,i,v,adj,vis):
        for j in adj[i]:
            if vis[j]==-1:
                vis[j]=1
                self.dfs(j,v,adj,vis)
                self.stack.append(j)
#{ 
#  Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends