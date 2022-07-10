class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        prev=[0 for i in range(2*k+1)]
        curr=prev.copy()
        
        for ind in range(len(prices)-1,-1,-1):
            for trans in range(2*k-1,-1,-1):
                
                if trans%2==0:
                    prev[trans]=max( -prices[ind]+curr[trans+1], curr[trans])
                else:
                    prev[trans]=max(prices[ind]+curr[trans+1], curr[trans])
            curr=prev
        return prev[0]