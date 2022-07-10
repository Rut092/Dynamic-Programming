class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[-9999 for i in range(len(prices)+1)] for j in range(2)]
        
        def f(ind,buy):
            
            if dp[buy][ind]!=-9999:
                return dp[buy][ind]
            
            if ind==len(prices):
                return 0
            
            
            
            elif buy:
                profit=max(-prices[ind]+f(ind+1,0),f(ind+1,1))
            
            else:
                profit=max(prices[ind]+f(ind+1,1),f(ind+1,0))
           
            dp[buy][ind]=profit
            return profit
        
        return f(0,1)