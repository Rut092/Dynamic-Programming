class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[[-9999 for p in range(3)] for i in range(len(prices)+1)] for j in range(2)]
        
        def f(ind,buy,cap):
            
            if cap==0:
                return 0
            
            if ind==len(prices):
                return 0
            
            elif dp[buy][ind][cap]!=-9999:
                return dp[buy][ind][cap]
            
            else:
                if buy:
                    profit= max(-prices[ind]+f(ind+1,0,cap),f(ind+1,1,cap))
                    
                else:
                    profit= max(prices[ind]+f(ind+1,1,cap-1),f(ind+1,0,cap))
                    
                dp[buy][ind][cap]= profit
                return profit
            
            
            
        return f(0,1,2)