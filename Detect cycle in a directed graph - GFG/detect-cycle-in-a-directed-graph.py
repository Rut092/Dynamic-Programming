#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        indeg=[0 for i in range(V)]
        vis=indeg.copy()
        for i in adj:
            for j in i:
                indeg[j]+=1
        queue=[]
        for i in range(V):
            if indeg[i]==0:
                vis[i]=1
                queue.append(i)
        p=0
        while(1):
            if p<len(queue):
                for i in (adj[queue[p]]):
                    indeg[i]-=1
                    if indeg[i]==0:
                        if vis[i]==0:    
                            vis[i]=1
                            queue.append(i)
                p+=1
            else:
                break
        if len(queue)==V:
            return False
        return True
        
        
        
        
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