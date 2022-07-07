class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp= [[-1 for i in range(len(text2))] for j in range(len(text1))]
        
        def lcs(ind1,ind2):
            if ind1<0 or ind2<0:
                return 0
            
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            
            elif text1[ind1]==text2[ind2]:
                a=1+lcs(ind1-1,ind2-1)
                dp[ind1][ind2]=a
                return a
            
            else:
                a=max(lcs(ind1-1,ind2),lcs(ind1,ind2-1))
                dp[ind1][ind2]=a
                return a
            
        return lcs(len(text1)-1,len(text2)-1)