#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        rep=None
        mis=None
        p=[0 for i in range(n)]
        for i in arr:
            p[i-1]+=1
            if p[i-1]==2:
                rep=i
        
        for i in range(n):
            if p[i]==0:
                mis=i+1
        
        return [rep,mis]
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends