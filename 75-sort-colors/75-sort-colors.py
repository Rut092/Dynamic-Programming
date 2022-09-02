import math
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=0
        for p in nums:
            if p==0:
                i+=1
            elif p==1:
                j+=1
                
        for p in range(len(nums)):
            if i>0:
                nums[p]=0
                i-=1
            elif j>0:
                nums[p]=1
                j-=1
            else:
                nums[p]=2