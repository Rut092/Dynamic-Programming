class Solution:
    def countVowelStrings(self, n: int) -> int:
        temp=["a","e","i","o","u"]
        
        dp=[[0 for i in range(n+1)] for i in range(5)]
        
        def fun(ind,count):
            
            if ind>4:
                return 0
            if count==0:
                return 1
            if ind==4 and count==1:
                return 1
            
            if dp[ind][count]!=0:
                return dp[ind][count]
            else:
                a=fun(ind,count-1)
                b=fun(ind+1,count)
                
                dp[ind][count]=a+b
                
                return dp[ind][count]
            
        return fun(0,n)