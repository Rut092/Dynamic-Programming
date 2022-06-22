#User function Template for python3
class Solution:
	def minDifference(self, nums, n):
		# code here
		tot_sum=sum(nums)
        dp=([[False for i in range(tot_sum+1)] for i in range(len(nums)+1)])
        
        for i in range(len(nums)):
            dp[i][0]=True
        
        for ind in range(1,len(nums)+1):
            for tar in range(1,tot_sum+1):
                if tar<nums[ind-1]:
                    dp[ind][tar]=dp[ind-1][tar]
                if tar>=nums[ind-1]:
                    dp[ind][tar]=(dp[ind-1][tar] or dp[ind-1][tar-nums[ind-1]])
        
        ans=tot_sum
        for i in range(len(dp[0])):
            if dp[len(nums)][i]==True:
                ans=min(ans,abs((tot_sum-i)-i))
        return ans        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends