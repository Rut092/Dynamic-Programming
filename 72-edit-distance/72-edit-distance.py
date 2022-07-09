class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[-1 for i in range(len(word2))] for j in range(len(word1))]
        
        def rec(ind1,ind2):
            if ind1<0:
                return ind2+1
            if ind2<0:
                return ind1+1
            
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if word1[ind1]==word2[ind2]:
                dp[ind1][ind2]=rec(ind1-1,ind2-1)
                return dp[ind1][ind2]
            
            else:
                dp[ind1][ind2]=1+min(rec(ind1-1,ind2),rec(ind1,ind2-1),rec(ind1-1,ind2-1))
                return dp[ind1][ind2]
            
        return rec(len(word1)-1,len(word2)-1)