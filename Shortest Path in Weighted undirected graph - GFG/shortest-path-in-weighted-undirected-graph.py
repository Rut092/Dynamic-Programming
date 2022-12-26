#User function Template for python3
import heapq

class Solution:
    def shortestPath(self, n, m, edges):
        # Code here
        adj=[[] for i in range(0,n+1)]
        
        for i in edges:
            adj[i[0]].append([i[1],i[2]])
            adj[i[1]].append([i[0],i[2]])
        
        que=[[0,1,[1]]]
        heapq.heapify(que)
        
        stack=[]
        
        dist=[2**32 for i in range(n+1)]
        
        dist[0]=0
        dist[1]=0
        
        while(len(que)>0):
            a,b,c=heapq.heappop(que)
            for i in adj[b]:
                
                if dist[i[0]]>a+i[1]:
                    dist[i[0]]= a+i[1]
                    heapq.heappush(que,[a+i[1],i[0],c+[i[0]]])

                    if i[0]==n:
                        stack.append(c+[i[0]])
                    
        
        if dist[-1]==2**32:
            return [-1]
        return stack[-1]
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, m = list(map(int, input().split()))
        edges = []
        for i in range(m):
            node1, node2, weight = list(map(int, input().split()))
            edges.append([node1, node2, weight])
        obj = Solution()
        ans = obj.shortestPath(n, m, edges)
        for e in ans:
            print(e, end = ' ')
        print()
# } Driver Code Ends