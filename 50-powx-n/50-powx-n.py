class Solution:
    def myPow(self, x: float, n: int) -> float:
        pow=abs(n)
        y=1.00000
        
        while(pow>0):
            if pow%2==1:
                y*=x
                pow-=1
            else:
                x*=x
                pow/=2
            
        if n<0:
            return round(1/y,5)
        else:
            return round(y,5)
                