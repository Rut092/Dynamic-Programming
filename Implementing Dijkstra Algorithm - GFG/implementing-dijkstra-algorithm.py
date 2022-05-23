class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        dis_node=[[0,S]]
        dist=[999999 for i in range(V)]
        dist[S]=0
        
        
        while(len(dis_node)>0):
            x,y=dis_node[0]
            for i in adj[y]:
                if dist[i[0]]>x+i[1]:
                    dist[i[0]]=x+i[1]
                    dis_node.append([x+i[1],i[0]])
            dis_node.pop(0)
            dis_node=sorted(dis_node,key= lambda x:x[0])      
        
        return (dist)
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends