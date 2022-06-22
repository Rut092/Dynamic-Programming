class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp=[[-1 for i in range(sum(nums)//2+1)] for j in range(len(nums)+1)]
        
        def fun(ind,target):
            if dp[ind][target]!=-1:
                return dp[ind][target]
            if target==0:
                return True
            if ind==0:
                return nums[0]==target
            
            not_take=fun(ind-1,target)
            take=False
            if target>=nums[ind]:
                take=fun(ind-1,target-nums[ind])
            
            dp[ind][target]=take or not_take
            return take or not_take
        
        if sum(nums)%2==1:
            return False
        return fun(len(nums)-1,sum(nums)//2)
        
        