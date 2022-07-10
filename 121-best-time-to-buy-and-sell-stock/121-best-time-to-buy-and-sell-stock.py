class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit=0
        mini=prices[0]
        for i in prices:
            cost=i-mini
            profit=max(profit,cost)
            mini=min(i,mini)
        return profit