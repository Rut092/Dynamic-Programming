class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(len(nums)):
            a=target-nums[i]
            if a in dict:
                return [dict[a],i]
            else:
                dict[nums[i]]=i
                
                