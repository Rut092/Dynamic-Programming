#User function Template for python3

from typing import List
from collections import defaultdict
import sys
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        #Your code here
        
        dist=[2**32 for i in range(n)]
        dist[0]=0
        
        ways=[0 for i in range(n)]
        
        adj=[[] for i in range(n)]
        
        for i in roads:
            adj[i[0]].append([i[1],i[2]])
            adj[i[1]].append([i[0],i[2]])
        
        que=[[0,0]]
        
        while(len(que)>0):
            
            a,b=heapq.heappop(que)
            
            for i in adj[b]:
                
                temp=a+i[1]
                
                if temp==dist[i[0]]:
                    ways[i[0]]+=ways[b]
                
                elif temp<dist[i[0]]:
                    ways[i[0]]=1
                    dist[i[0]]=temp
                    que.append([temp,i[0]])
                    
        
        return ways[-1]%(10**9+7)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        adj=[]
        
        for i in range(m):
            tmp =[]
            x,y,z=map(int,input().split())
            tmp.append(x)
            tmp.append(y)
            tmp.append(z)
            adj.append(tmp)
            
        
        
        
       
        obj = Solution()
        res = obj.countPaths(n, adj)
        
        print(res)
        

# } Driver Code Ends