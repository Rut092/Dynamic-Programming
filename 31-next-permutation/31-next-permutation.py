class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return 
        x=len(nums)-2
        while(x>=0 and nums[x]>=nums[x+1]):
            x-=1
        if x<0:
            nums[:]=nums[::-1]
        else:
            z=len(nums)-1
            while(nums[z]<=nums[x]):
                z-=1
            nums[z],nums[x]=nums[x],nums[z]
            nums[x+1:]=reversed(nums[x+1:])
            