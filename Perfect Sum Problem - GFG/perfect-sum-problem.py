#User function Template for python3
class Solution:
	def perfectSum(self, num, n, sum):
		# code here
		zeros=0
		arr=[]
		for i in num:
		    if i==0:
		        zeros+=1
		    else:
		        arr.append(i)
		n=len(arr)
		        
        dp=[[-1 for i in range(sum+1)] for i in range(n+1)]
        
        def fun(ind,target):
            if target==0:
                return 1
            if ind==0:
                if target==arr[0]:
                    return 1
                else:
                    return 0
            
            if dp[ind][target]!=-1:
                return dp[ind][target]
                
            if target>=arr[ind]:
                dif=fun(ind-1,target)+fun(ind-1,target-arr[ind])
            else:
                dif=fun(ind-1,target)
                
            dp[ind][target]=dif
            
            return dif
            
        return ((2**zeros)*fun(n-1,sum))%(10**9+7)
        
        
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends