class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        temp=cost+[0]
        dp=[0 for i in range(n+1)]
        def mini(ind):
            if ind<0:
                return 0
            elif dp[ind]!=0:
                return dp[ind]
            else:
                dp[ind]=temp[ind]+min(mini(ind-1),mini(ind-2))
                return dp[ind]
    
        return mini(n)