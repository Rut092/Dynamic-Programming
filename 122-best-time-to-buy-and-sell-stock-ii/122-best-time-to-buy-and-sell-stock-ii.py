class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[0 for i in range(len(prices)+1)] for j in range(2)]
        
        
        
        for ind in range(len(prices)-1,-1,-1):
            for buy in range(2):
                if buy:
                    profit=max(-prices[ind]+dp[0][ind+1],dp[1][ind+1])
                else:
                    profit=max(prices[ind]+dp[1][ind+1],dp[0][ind+1])
                    
                dp[buy][ind]=profit
                
        return dp[1][0]
        
        