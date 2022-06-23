#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        # code here
        dp=[[-1 for i in range(W+1)] for j in range(n)]
        
        def fun(ind,weight):
            if weight==0:
                return 0
            if ind==0:
                if weight>=wt[ind]:
                    return val[ind]
                    
                else:
                    return 0
                    
            if dp[ind][weight]!=-1:
                return dp[ind][weight]
            
            not_take=fun(ind-1,weight)
            take=0
            
            if weight>=wt[ind]:
                take=val[ind]+fun(ind-1,weight-wt[ind])
                
            dp[ind][weight]= max(take,not_take)
            
            return dp[ind][weight]
            
        return fun(n-1,W)
        

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