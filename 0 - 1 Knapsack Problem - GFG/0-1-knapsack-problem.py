#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        dp=[[0 for i in range(W+1)] for i in range(n)]
        
        
        for index in range(n):
            for weight in range(W+1):
                if index==0 or weight==0:
                    if index==0 and wt[0]<=weight:
                        dp[index][weight]= val[0]
                    else:
                        dp[index][weight]= 0
                        
                else:
                    a=0
                    if wt[index]<=weight:
                        a=val[index]+dp[index-1][weight-wt[index]]
                    b=dp[index-1][weight]
                      
                    dp[index][weight]=max(a,b)  
                
        return dp[-1][-1]

#{ 
 # Driver Code Starts
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