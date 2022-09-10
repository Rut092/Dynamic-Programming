class Solution:
    def tribonacci(self, n: int) -> int:
        t1=0
        t2=1
        t3=1
        
        if n==0:
            return 0
        if n==2:
            return 1
        
        for i in range(3,n+1):
            temp=t1+t2+t3
            t1=t2
            t2=t3
            t3=temp
        return t3