class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        dp=[[-1 for i in range(m)] for j in range(n)]
        def f(ind1,ind2):
            if ind1==n or ind2==m:
                return 0
            
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            
            if text1[ind1]==text2[ind2]:
                dp[ind1][ind2]= f(ind1+1,ind2+1)+1
                return dp[ind1][ind2]
            else:
                dp[ind1][ind2]=max(f(ind1+1,ind2),f(ind1,ind2+1))
                return dp[ind1][ind2]
                
        return f(0,0)