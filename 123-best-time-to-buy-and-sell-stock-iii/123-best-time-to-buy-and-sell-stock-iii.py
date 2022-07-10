class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[[0 for p in range(3)] for i in range(len(prices)+1)] for j in range(2)]
        
        for ind in range(len(prices)-1,-1,-1):
            for buy in range(2):
                for cap in range(1,3):
                    
                    if buy:
                        dp[buy][ind][cap]=max(-prices[ind]+dp[0][ind+1][cap],dp[1][ind+1][cap])
                    else:
                        dp[buy][ind][cap]=max(prices[ind]+dp[1][ind+1][cap-1],dp[0][ind+1][cap])
                        
        return dp[1][0][2]