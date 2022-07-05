#User function Template for python3

class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        dp= [[0 for i in range(W+1)] for j in range(N)]
        
        for tar in range(W+1):
            if tar>=wt[0]:
                dp[0][tar]=(tar//wt[0])*val[0]
        
        for ind in range(1,N):
            for tar in range(1,W+1):
                
                not_take=dp[ind-1][tar]
                take=0
                if tar>=wt[ind]:
                    take=dp[ind][tar-wt[ind]]+val[ind]
                
                dp[ind][tar]=max(take,not_take)
                
        return dp[-1][-1]
                
        
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends