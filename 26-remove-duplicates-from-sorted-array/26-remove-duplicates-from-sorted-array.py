class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=0
        arr=[]
        for i in nums:
            if i not in arr:
                arr.append(i)
        for i in range(len(arr)):
            nums[i]=arr[i]
        
        return len(arr)