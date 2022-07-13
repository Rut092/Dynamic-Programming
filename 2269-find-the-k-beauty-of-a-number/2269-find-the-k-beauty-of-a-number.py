class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        mini=0
        a=str(num)
        n=len(a)
        for i in range(0,n-k+1):
            if int(a[i:i+k])!=0 and num%int(a[i:i+k])==0:
                mini+=1 
        return mini