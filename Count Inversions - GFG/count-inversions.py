class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        # Your Code Here
        
        self.inv=0
        
        def partition(arr1,arr2):
        
            temp=[]
            
            l1=len(arr1)
            l2=len(arr2)
            
            p1=0
            p2=0
            
            while(p1<l1 or p2<l2):
                
                if p1<l1 and p2<l2: 
                    
                    if arr1[p1]>arr2[p2]:
                        temp.append(arr2[p2])
                        self.inv+=l1-p1
                        p2+=1
                    
                    else:
                         
                        temp.append(arr1[p1])
                        p1+=1
                        
                else:
                    
                    if p1>=l1:
                        
                        temp+=arr2[p2:]
                        
                    else:
                        temp+=arr1[p1:]
                        
                    #print(self.inv)
                    return temp
        
        
        def divide(arr):
            
            l=len(arr)
            
            if l<=1:
                return arr
            
            else:
                mid = l//2
                
                p=divide(arr[:mid]) 
        
                q=divide(arr[mid:]) 
                
                return partition(p,q)
                
            
        divide(arr)
        return self.inv
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends