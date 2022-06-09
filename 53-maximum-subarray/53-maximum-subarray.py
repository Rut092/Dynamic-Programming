class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #this is Kadane's Algorithm
        
        sum=nums[0]
        cur=0
        
        for i in nums:
            a=cur+i
            if a>=0:
                cur+=i
            else:
                cur=0
            if cur>sum and cur!=0:
                sum=cur
            if i>sum:
                sum=i
        return sum