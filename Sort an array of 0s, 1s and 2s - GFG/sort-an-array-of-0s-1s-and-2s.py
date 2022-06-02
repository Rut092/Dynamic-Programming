#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        low=0
        high=n-1
        mid=0
        
        while(high>=mid):
            
            if arr[mid]==0 and arr[low]==0:
                mid+=1
                low+=1
            
            elif arr[low]==1 and arr[mid]==0:
                arr[low],arr[mid]=arr[mid],arr[low]
                low+=1
                mid+=1
                
            elif arr[low]==1 and arr[mid]==1:
                mid+=1
            
            elif arr[mid]==2 and arr[high]==0:
                arr[mid],arr[high]=arr[high],arr[mid]
                high-=1
            
            elif arr[mid]==2 and arr[high]==1:
                arr[high],arr[mid]=arr[mid],arr[high]
                high-=1
                
            elif arr[high]==2 and arr[mid]==2:
                high-=1
            
            else:
                mid+=1
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends