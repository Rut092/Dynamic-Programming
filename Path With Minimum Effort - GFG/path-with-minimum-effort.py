#User function Template for python3
import heapq

class Solution:
        
    def MinimumEffort(self, arr):
        #code here
        
        li,lo=len(arr[0]),len(arr)
        
        dis=[[2**32 for i in range(li)] for i in range(lo)]
        dis[0][0]=0
        
        que=[[0,0,0]]
        
        l1=[-1,0,0,1]
        l2=[0,-1,1,0]
        
        while(len(que)>0):
            c,a,b=heapq.heappop(que)
            
            for i in range(4):
                
                row,col=a+l1[i],b+l2[i]
                
                if row>=0 and col>=0 and row<lo and col<li:
                    effort = max(c, abs(arr[row][col]-arr[a][b]))
                    
                    if effort<dis[row][col]:
                        dis[row][col]=effort
                        heapq.heappush(que,[effort,row,col])
                        
        return dis[-1][-1]
                    
                
                    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n,m=map(int,input().split())
        a=[]
        for i in range(n):
            li=list(map(int,input().split()))
            a.append(li)
        ob = Solution()
        ans = ob.MinimumEffort(a)
        print(ans)
        tc -= 1
# } Driver Code Ends