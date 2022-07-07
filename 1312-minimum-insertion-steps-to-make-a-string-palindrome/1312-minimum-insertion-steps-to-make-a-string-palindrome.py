class Solution:
    def minInsertions(self, s: str) -> int:
        S1=s
        S2=S1[::-1]
        n=len(s)
        dp=[[0 for i in range(n+1)] for j in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                
                if S1[i-1]==S2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                    
                
        return n-dp[-1][-1]