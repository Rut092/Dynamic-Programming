class Solution:
    def climbStairs(self, n: int) -> int:
        curr=1
        prev=1
        temp=None
        if n==1:
            return 1
        for i in range(2,n+1):
            temp=curr+prev
            prev,curr=curr,temp
        return curr