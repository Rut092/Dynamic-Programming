class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        if len(nums)==1:
            return nums
        else:
            a=len(nums)-2
            while(a>=0 and nums[a]>=nums[a+1]):
                a-=1
            if a<0:
                nums[:]=nums[::-1]
            else:
                b=len(nums)-1
                while(nums[a]>=nums[b]):
                    b-=1
                nums[a],nums[b]=nums[b],nums[a]
                nums[a+1:]=reversed(nums[a+1:])
                return nums