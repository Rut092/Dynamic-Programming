class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        indeg=[0 for i in range(V)]
        for i in adj:
            for j in i:
                indeg[j]+=1
        q=[]
        vis=[-1 for i in range(V)]
        p=0
        for i in range(V):
            if indeg[i]==0:
                vis[i]=1
                q.append(i)
        while(1):
            if p<len(q):
                for i in adj[q[p]]:
                    indeg[i]-=1
                    if indeg[i]==0:
                        if vis[i]==-1:
                            vis[i]=1
                            q.append(i)
                p+=1
            else:
                break
        return q
        
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