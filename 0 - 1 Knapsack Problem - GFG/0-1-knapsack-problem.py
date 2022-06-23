#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        # code here
        dp=[[0 for i in range(W+1)] for j in range(n)]
        
        for ind in range(n):
            for weight in range(W+1):
                
                if weight==0:
                    dp[ind][weight]=0
                    
                elif ind==0:
                    if weight>=wt[ind]:
                        dp[ind][weight]=val[ind]
                        
                else:
                    not_take=dp[ind-1][weight]
                    take=0
                    
                    if weight>=wt[ind]:
                        take=dp[ind-1][weight-wt[ind]]+val[ind]
                    
                    dp[ind][weight]=max(take,not_take)
        
        return dp[-1][-1]
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends