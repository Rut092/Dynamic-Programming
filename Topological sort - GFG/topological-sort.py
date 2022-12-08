class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        
        indeg=[0 for i in range(V)]
        #vis=[0 for i in range(V)]
        
        for i in adj:
            for j in i:
                indeg[j]+=1
                
        que=[]
        
        for i in range(V):
            if indeg[i]==0:
                que.append(i)
            
        i=0    
        while(len(que)>i):
            a=que[i]
            i+=1
            
            for j in adj[a]:
                indeg[j]-=1
                if indeg[j]==0:
                    que.append(j)
            
        return que
            
            
        

#{ 
 # Driver Code Starts
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