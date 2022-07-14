class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=0
        num=0
        for i in nums:
            if i==1:
                num+=1
            else:
                maxi=max(maxi,num)
                num=0
            
        return max(maxi,num)