class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)>1:
            self.num=nums[:-1]
            length=len(self.num)
            self.arr=[-1]*(length)
            self.p1(length-1)
            ans1=self.arr[-1]

            self.arr=[-1]*(length)
            self.num=nums[1:]
            self.p1(length-1)
            ans2=self.arr[-1]
            ans=max(ans1,ans2)
            return ans
        else:
            return nums[0]
        
    def p1(self,n):
        if n<0:
            return 0
        if n==0:
            self.arr[n]=self.num[0]
            return self.num[0]
            
        if n==1:
            z=max(self.num[0],self.num[1])
            self.arr[n]=z
            return z
        
        if self.arr[n-2]!=-1:
            a=self.arr[n-2]+self.num[n]
        else:
            a=self.p1(n-2)+self.num[n]
        
        if self.arr[n-1]!=-1:
            b=self.arr[n-1]
        else:
            b=self.p1(n-1)
            
        maxi=max(a,b)
        self.arr[n]=maxi
        
        return maxi
        
        