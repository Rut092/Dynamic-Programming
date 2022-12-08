#User function Template for python3

from typing import List

class Solution:    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        # code here
        
        adj1 = [[] for i in range(V)]
        
        for i in range(V):
            for j in (adj[i]):
                adj1[j].append(i)
                
        indeg=[0 for i in range(V)]
        
        arr=[0 for i in range(V)]
        
        for i in adj1:
            for j in i:
                indeg[j]+=1
                
        que=[]
        
        for i in range(V):
             if indeg[i]==0:
                 que.append(i)
                 arr[i]=1
                 
        i=0
        while(len(que)>i):
            a=que[i]
            i+=1
            
            for j in adj1[a]:
                indeg[j]-=1
                
                if indeg[j]==0:
                    que.append(j)
                    arr[j]=1
        
        ans=[]
        for i in range(V):
            if arr[i]==1:
                ans.append(i)
        
        return ans
                
                
                
                
                
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end = ' ')
        print()
            


# } Driver Code Ends