#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        #code here
        dist=[10**8 for i in range(V)]
        dist[S]=0
        
        for i in range(V):
            for j in edges:
                a,b,c=j
                if dist[a]+c<dist[b]:
                    dist[b]=dist[a]+c
                    
        # because we cannot reduce at Nth iteration
        for j in edges:
            a,b,c=j
            if dist[a]+c<dist[b]:
                return [-1]
        
            
        return dist
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        edges = []
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            edges.append([u,v,w])
        S=int(input())
        ob = Solution()
        
        res = ob.bellman_ford(V,edges,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends