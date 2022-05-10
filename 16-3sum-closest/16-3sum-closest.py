class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans=999999
        val=0
        arr=sorted(nums)
        print(arr)
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while(j<k):
                abc=(abs((arr[i]+arr[j]+arr[k])-target))
                if abc<ans:
                    ans=abc
                    val=arr[i]+arr[j]+arr[k]
                if arr[i]+arr[j]+arr[k]>target:
                    k-=1
                elif arr[i]+arr[j]+arr[k]<target:
                    j+=1
                else:
                    ans=0
                    break
            if ans==0:
                break
        return val