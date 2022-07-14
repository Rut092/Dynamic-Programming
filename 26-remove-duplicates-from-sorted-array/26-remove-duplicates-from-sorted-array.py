class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        for j in range(1,n):
            if nums[i]!=nums[j]:
                nums[i+1]=nums[j]
                i+=1
        for j in range(i+1,n):
            nums.pop(-1)