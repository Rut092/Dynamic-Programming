class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp=[1]
        p1=0
        p2=0
        p3=0
        for i in range(1,n):
            dp.append(min(2*dp[p1],3*dp[p2],5*dp[p3]))
            if dp[i]==2*dp[p1]:
                p1+=1
            if dp[i]==3*dp[p2]:
                p2+=1
            if dp[i]==5*dp[p3]:
                p3+=1
        return dp[n-1]