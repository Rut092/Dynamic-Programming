class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        prev=[0 for i in range(2)]
        curr=prev.copy()
        
        for ind in range(len(prices)-1,-1,-1):
                prev[1]=max( -prices[ind]+curr[0],curr[1])
                
                prev[0]=max( prices[ind]+curr[1]-fee,curr[0])
                curr=prev
        return prev[1]