#User function Template for python3

class Solution:
    def findOrder(self, n, m, prerequisites):
        # Code here
        adj=[[] for i in range(n)]
        V=n
        for i in prerequisites:
            adj[i[1]].append(i[0])
        
        #print(adj)
        
        indeg=[0 for i in range(V)]
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
        
        #print(que)
        return que if len(que)==V else []


#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
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
        n,m = list(map(int, input().strip().split()))
        adj = [[] for i in range(n)]
        prerequisites = []
        
        for i in range(m):
            u,v=map(int,input().split())
            adj[v].append(u)
            prerequisites.append([u,v])
            
        ob = Solution()
        
        res = ob.findOrder(n, m, prerequisites)
        
        if(not len(res)):
            print("No Ordering Possible")
        else:
            if check(adj, n, res):
                print(1)
            else:
                print(0)
# } Driver Code Ends