#User function Template for python3

class Solution:
    def count(self, S, m, n): 
        # code here 
        dp= [[0 for i in range(n+1)] for j in range(m)]
        
        for target in range(n+1):
            if target%S[0]==0:
                dp[0][target]=1
                
        for ind in range(1,m):
            for tar in range(0,n+1):
                
                not_take=dp[ind-1][tar]
                take=0
                if tar>=S[ind]:
                    take=dp[ind][tar-S[ind]]
                    
                dp[ind][tar]=take+not_take
                
        return dp[-1][-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().strip().split()))
        S = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(S,m,n))
# } Driver Code Ends