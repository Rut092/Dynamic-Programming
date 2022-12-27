#User function Template for python3
from typing import List

class Solution:
    def CheapestFLight(self,n,flights,src,dst,k):
        
        que=[[0,src,0]]
        adj=[[] for i in range(n)]
        
        for i in flights:
            adj[i[0]].append([i[1],i[2]])
            
        path=[2**32 for i in range(n)]
        path[src]=0
        
        p=0
        while(len(que)>p):
            stop,node,dist=que[p]
            p+=1
            
            if stop<k+1:
                if node==dst:
                    continue
                else:
                    for i in adj[node]:
                        if path[i[0]]>dist+i[1]:
                            path[i[0]]=dist+i[1]
                            que.append([stop+1,i[0],dist+i[1]])
                         
        if path[dst]==2**32:
            return -1
        return path[dst]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range (test_cases):
        n,edge=map(int,input().split())
        flights=[]
        for _ in range(edge):
            temp=list(map(int,input().split()))
            flights.append(temp[:])
        src=int(input())
        dst=int(input())
        k=int(input())
        obj=Solution()
        res=obj.CheapestFLight(n,flights,src,dst,k)
        print(res)

        
        
# } Driver Code Ends