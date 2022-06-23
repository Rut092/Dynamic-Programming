#User function Template for python3
class Solution:
	def minCoins(self, coins, M, V):
		# code here
		n=M
        dp=[[1e9 for i in range(V+1)] for j in range(n)]
        
        for target in range(V+1):
            if target%coins[0]==0:
                dp[0][target]=target//coins[0]
        
        for ind in range(1,n):
            for target in range(V+1):
                        
                not_take=dp[ind-1][target]
                take=1e9
                
                if target>=coins[ind]:
                    take=dp[ind][target-coins[ind]]+1
                    
                dp[ind][target]=min(take,not_take)
        #print(dp)
        if dp[-1][-1]==1e9:
            return -1
        return dp[-1][-1]
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		v,m = input().split()
		v,m = int(v), int(m)
		coins = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minCoins(coins,m,v)
		print(ans)

# } Driver Code Ends