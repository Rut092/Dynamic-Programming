class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr=[0,0]
        prev=[0,0]
        
        
        
        for ind in range(len(prices)-1,-1,-1):
            for buy in range(2):
                if buy:
                    profit=max(-prices[ind]+curr[0],curr[1])
                else:
                    profit=max(prices[ind]+curr[1],curr[0])
                    
                prev[buy]=profit
            curr=prev
        return prev[1]
        
        