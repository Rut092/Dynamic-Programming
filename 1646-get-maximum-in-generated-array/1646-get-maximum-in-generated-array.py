class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        dp=[0 for i in range(n+1)]
        maxi=1
        if n==0:
            return 0
        
        dp[1]=1
        
        for i in range(2,n+1):
            if i%2==0:
                dp[i]=dp[i//2]
            else:
                dp[i]=dp[i//2]+dp[(i//2)+1]
            
            maxi=max(dp[i],maxi)
        return maxi