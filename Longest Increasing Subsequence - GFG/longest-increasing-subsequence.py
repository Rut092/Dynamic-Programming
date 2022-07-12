#User function Template for python3

class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        # code here
       
        dp=[[-1 for i in range(n)] for j in range(n)]
        
        def ls(ind,prev):
            if ind==n:
                return 0
            if dp[ind][prev+1]!=-1:
                return dp[ind][prev+1]
            else:
                z=0
                if prev==-1 or a[ind]>a[prev]:
                    z= 1+ls(ind+1,ind)
                b=ls(ind+1,prev)
                
                dp[ind][prev+1]=max(z,b)
                return max(z,b)
        return ls(0,-1)
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
# } Driver Code Ends