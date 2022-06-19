class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=2**32
        profit=0
        
        for i in prices:
            if i<mini:
                mini=i
            if i-mini>profit:
                profit=i-mini
        return profit