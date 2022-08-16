class Solution:
    def isUgly(self, n: int) -> bool:
        if n==0:
            return False
        temp=n
        while(temp%2==0 or temp%3==0 or temp%5==0):
            if temp%2==0:
                temp//=2
            if temp%3==0:
                temp//=3
            if temp%5==0:
                temp//=5
                
        return True if temp==1 else False