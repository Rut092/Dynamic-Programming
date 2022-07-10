class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp=[[0 for i in range(2)]for j in range(len(prices)+2)]
        
        for ind in range(len(prices)-1,-1,-1):
            for buy in range(2):
                
                if buy:
                    dp[ind][buy]=max( -prices[ind]+dp[ind+1][0],dp[ind+1][1])
                else:
                    dp[ind][buy]=max( prices[ind]+dp[ind+2][1],dp[ind+1][0])
        return dp[0][1]