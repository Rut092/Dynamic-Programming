#User function Template for python3
class Solution:
    def minDeletions(self, Str, n): 
        #code here
        S1=Str
        S2=S1[::-1]
        
        dp=[[0 for i in range(n+1)] for j in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                
                if S1[i-1]==S2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                    
                
        return n-dp[-1][-1]
            
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
       
        N = int(input())
        Str = input().strip()
        ob = Solution()
        ans = ob.minDeletions(Str, N)
        print(ans)
# } Driver Code Ends