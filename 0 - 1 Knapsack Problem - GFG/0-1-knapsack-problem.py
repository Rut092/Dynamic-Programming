#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        dp=[[0 for i in range(W+1)] for i in range(n)]
        
        def f(index,weight):
            if index==0 or weight==0:
                if index==0 and wt[0]<=weight:
                    return val[0]
                
                else:
                    return 0
            
            if dp[index][weight]!=0:
                return dp[index][weight]
            
            a=0
            if wt[index]<=weight:
                a=val[index]+f(index-1,weight-wt[index])
                
            b=f(index-1,weight)
              
            dp[index][weight]=max(a,b)      
            return dp[index][weight]
            
        return f(n-1,W)
            

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