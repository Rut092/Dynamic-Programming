#User function Template for python3

class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        
        adj=[[] for i in range(n)]
        
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
            
        dist=[-1 for i in range(n)]
        dist[src]=0
        
        que=[src]
        i=0
        
        while(i<len(que)):
            a=que[i]
            i+=1
            
            for j in adj[a]:
                
                if dist[j]==-1:
                    dist[j]=1+dist[a]
                    que.append(j)
                    
                elif dist[j]>1+dist[a]:
                    dist[j]=1+dist[a]
                    que.append(j)
             
        return dist
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends