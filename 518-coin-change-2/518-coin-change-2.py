class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp= [[1e9 for i in range(amount+1)] for j in range(len(coins))]
        
        def ways(ind,target):
            
            if ind==0:
                
                if target%coins[0]==0:
                    return 1
                
                return 0
            
            if dp[ind][target]!=1e9:
                return dp[ind][target]
            
            
            not_take=ways(ind-1,target)
            take=0
            if target>=coins[ind]:
                take=ways(ind,target-coins[ind])
            
            dp[ind][target]=take+not_take
            
            return dp[ind][target]
        
        
        return ways(len(coins)-1,amount)
    