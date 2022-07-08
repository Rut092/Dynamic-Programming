#User function Template for python3
class Solution:
	def minOperations(self, A, B):
		# code here
        dp=[[0 for i in range(len(B)+1)] for j in range(len(A)+1)]
        
        for i in range(1,len(A)+1):
            for j in range(1,len(B)+1):
                
                if A[i-1]==B[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                    
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        
        
        return max(len(A),len(B))-2*dp[-1][-1]+min(len(A),len(B))
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s1,s2 = input().split()
		ob = Solution()
		ans = ob.minOperations(s1,s2)
		print(ans)
# } Driver Code Ends