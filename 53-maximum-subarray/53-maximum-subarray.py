class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=-999999
        temp=0
        for i in nums:
            temp+=i
            maxi=max(maxi,temp)
            if temp<0:
                temp=0
        return maxi