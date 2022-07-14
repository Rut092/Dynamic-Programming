class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        if n>=1:
            sumi=sum(nums[0:k])
            j=0
            ans=sumi
            for i in range(k,n):
                sumi+=nums[i]
                sumi-=nums[j]
                j+=1
                ans=max(sumi,ans)
        
        return ans/k