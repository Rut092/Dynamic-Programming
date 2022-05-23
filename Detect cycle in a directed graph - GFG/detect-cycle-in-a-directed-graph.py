#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        vis=[0 for i in range(V)]
        dfsvis=[0 for i in range(V)]
        op=[]
        
        def dfs(ind):
            vis[ind]=1
            dfsvis[ind]=1
            
            for j in adj[ind]:
                if vis[j]==0:
                    dfs(j)
                else:
                    if dfsvis[j]==1:
                        op.append(True)
                        return 
            dfsvis[ind]=0
            
        for i in range(V):
            if vis[i]==0:
                if len(op)==0:
                    dfs(i)
                if len(op)>0:
                    return True
        return False
            
        
        
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends