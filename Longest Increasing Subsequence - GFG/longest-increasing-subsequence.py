#User function Template for python3

class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        # code here
       
        dp={}
        
        def ls(ind,ele):
            if ind==n:
                return 0
            try:
                return dp[str([ind,ele])]
            except:
                z=0
                if a[ind]>ele:
                    z= 1+ls(ind+1,a[ind])
                b=ls(ind+1,ele)
                
                dp[str([ind,ele])]=max(z,b)
                return max(z,b)
                
        #print(dp)
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