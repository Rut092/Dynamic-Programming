import math
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        k=len(nums)-1
        j=0
        while(j<=k):
            if nums[j]==0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1
                
            elif nums[j]==1:
                j+=1
                
            else:
                nums[k],nums[j]=nums[j],nums[k]
                k-=1
                
            print(nums)
        print(nums)