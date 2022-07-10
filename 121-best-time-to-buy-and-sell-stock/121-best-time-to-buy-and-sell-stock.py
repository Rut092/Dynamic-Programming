class Solution:
    def maxProfit(self, p: List[int]) -> int:
        
        profit=0
        mini=p[0]
        for i in range(1,len(p)):
            cost=p[i]-mini
            profit=max(profit,cost)
            mini=min(p[i],mini)
        return profit