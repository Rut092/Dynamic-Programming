class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        V=len(graph)
        adj=graph
        ans=True
        color=[-1 for l in range(V)]
        for m in range(V):
            if color[m]==-1:
                stack=[]
                i=0
                stack.append(m)
                color[m]=0
                while(V):
                    if i<len(stack):
                        for p in adj[stack[i]]:
                            if color[p]!=-1:
                                if color[p]==color[stack[i]] and p!=stack[i]:
                                    ans=False
                                    break
                            elif color[p]==-1:
                                if color[stack[i]]==0:
                                    color[p]=1
                                else:
                                    color[p]=0
                                stack.append(p)
                        i+=1
                    else:
                        break
                    V-=1    
        return ans
        