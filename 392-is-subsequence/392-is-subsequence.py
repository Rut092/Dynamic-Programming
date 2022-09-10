class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a=len(s)
        b=len(t)
        dp=[[0 for i in range(b)] for j in range(a)]
        
        
        def fun(ind1,ind2):
            if ind1<0 or ind2<0:
                return 0
            
            elif ind1==0 and ind2==0:
                if s[0]==t[0]:
                    return 1
                return 0
            
            elif dp[ind1][ind2]!=0:
                return dp[ind1][ind2]
            
            elif s[ind1]==t[ind2]:
                dp[ind1][ind2]=1+fun(ind1-1,ind2-1)
                return dp[ind1][ind2]
            
            else:
                dp[ind1][ind2] = max(fun(ind1-1,ind2) ,fun(ind1,ind2-1))
                return dp[ind1][ind2]
            
        x=fun(a-1,b-1)
        if a==x:
            return True
        else:
            return False