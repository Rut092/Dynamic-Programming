class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        maxi=max(len(s),len(p))
        dp=[[-1 for i in range(maxi+1)] for j in range(maxi+1)]
        
        def fun(i,j):
            
            if i<0 and j<0:
                return True
            
            if i>=0 and j<0:
                return False
            
            if i<0 and j>=0:
                for jj in range(j+1):
                    if p[jj]!='*':
                        dp[i][j]=False
                        return False
                dp[i][j]=True
                return True
            
            if dp[i][j]!=-1:
                return dp[i][j]
            
            elif p[j]==s[i] or p[j]=='?':
                dp[i][j]=fun(i-1,j-1)
                return dp[i][j]
            
            
            elif p[j]=='*':
                dp[i][j]=fun(i-1,j) or fun(i,j-1)
                return dp[i][j]
            else:
                dp[i][j]=False
                return False
            
        return fun(len(s)-1,len(p)-1)