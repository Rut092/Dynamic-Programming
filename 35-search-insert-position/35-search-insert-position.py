class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def bin(st,end):

            mid=(st+end)//2
            
            if st==end:
                return st
            
            elif nums[mid]==target:
                return mid
            else:
                if target>nums[mid]:
                    return bin(mid+1,end)
                else:
                    return bin(st,mid)
                
        if target>nums[-1]:
            return len(nums)
        elif target<nums[0]:
            return 0
        return bin(0,len(nums)-1)