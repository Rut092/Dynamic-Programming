#User function Template for python3

class Solution:
    def isPossible(self,N,prerequisites):
        
        adj=[[] for i in range(N)]
        V=N
        for i in prerequisites:
            adj[i[0]].append(i[1])
        
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
        return len(que)==V


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends