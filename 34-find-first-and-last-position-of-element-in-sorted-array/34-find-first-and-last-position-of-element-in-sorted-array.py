class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        m=len(nums)
        
        if m==0:
            return [-1,-1]
        if nums[0]==nums[-1] and nums[0]==target:
            return [0,m-1]
        if m==1 and nums[0]==target:
            return [0,0]
        
        def bin(st,ed):
            mid=(st+ed)//2
            
            if nums[st]==target:
                return st
            
            elif nums[ed]==target:
                return ed
            
            elif nums[mid]==target:
                return mid
            
            elif st==ed:
                return -1
            
            elif nums[mid]>target:
                return bin(st,mid)
            
            elif nums[mid]<target:
                return bin(mid+1,ed)
            
            else:
                return -1
        
        a=bin(0,m-1)
        
        if a==-1:
            return [-1,-1]
        else:
            print(a)
            i=a
            j=a
            
            while((i-1>=0 and nums[i-1]==target) or (j+1<m and nums[j+1]==target)):
                if i>0 and nums[i-1]==target:
                    i-=1
                if j<m-1 and nums[j+1]==target:
                    j+=1
            return [i,j]
            