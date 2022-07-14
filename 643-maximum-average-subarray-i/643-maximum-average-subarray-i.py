class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        if n>=4:
            sumi=sum(nums[0:k])
            ans=sumi/k
            j=0
            for i in range(k,n):
                sumi+=nums[i]
                sumi-=nums[j]
                j+=1
                ans=max(sumi/k,ans)
        else:
            return sum(nums)/n
        return ans