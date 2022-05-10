class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dict={}
        def sol(m,n):
            if m==0 and n==0:
                return 1
            if m<0 or n<0:
                return 0
            if (m,n) in dict:
                return dict[(m,n)]
            
            a=sol(m,n-1)
            b=sol(m-1,n)  
            dict[(m,n)]=a+b
            return a+b
        
        ans=sol(m-1,n-1)
        return ans