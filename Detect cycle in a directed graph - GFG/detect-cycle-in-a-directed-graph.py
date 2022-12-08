#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        indeg=[0 for i in range(V)]
        vis=[0 for i in range(V)]
        
        for i in adj:
            for j in i:
                indeg[j]+=1
        
        que=[]
        for i in range(V):
            if indeg[i]==0:
                que.append(i)
                vis[i]=1
        i=0
        while(len(que)>i):
            a=que[i]
            i+=1
            
            for j in adj[a]:
                indeg[j]-=1
                if indeg[j]==0:
                    que.append(j)
        
        #print(que)
        return len(que)!=V


#{ 
 # Driver Code Starts
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