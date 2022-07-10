class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp=[[0 for i in range(2*k+1)] for j in range(len(prices)+1)]
        
        for ind in range(len(prices)-1,-1,-1):
            for trans in range(2*k-1,-1,-1):
                
                if trans%2==0:
                    dp[ind][trans]=max( -prices[ind]+dp[ind+1][trans+1], dp[ind+1][trans])
                else:
                    dp[ind][trans]=max( prices[ind]+dp[ind+1][trans+1], dp[ind+1][trans])
        return dp[0][0]