#User function Template for python3

class Solution:
    
    def maximizeSum (self,a, n) : 
        #Complete the function
        
        d={}
        
        for i in a:
            d[i]=0
        for i in a:
            d[i]+=1
        
        temp=0
        for i in range(n-1,-1,-1):
            if d[a[i]]>0:
                temp+=a[i]
                d[a[i]]-=1
                try:
                    d[a[i]-1]-=1
                except:
                    pass
    
        return temp


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    ob=Solution()
    
    ans = ob.maximizeSum(arr, n)
    print(ans)

    





# } Driver Code Ends