class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            alpha=nums
            no=nums[i]
            alpha[i]=-99999999
            if target-no in alpha:
                return [i,alpha.index(target-no)]
                
                