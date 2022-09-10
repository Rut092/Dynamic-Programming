class Solution:
    def fib(self, n: int) -> int:
        t1=0
        t2=1
        if n==0:
            return t1
        for i in range(2,n+1):
            temp=t1+t2
            t1=t2
            t2=temp
            
        return t2