#User function Template for python3

class Solution:
    def merge(self,left,right):
        # code here
        so=[]
        i=0
        j=0
        while(i<len(left) and j<len(right)):
            if left[i]<=right[j]:
                so.append(left[i])
                i+=1
            elif left[i]>right[j]:
                so.append(right[j])
                j+=1
        if len(left)>i:
            so+=left[i:]
        elif len(right)>j:
            so+=right[j:]
        return so
        
        
    def mergeSort(self,arr, l, r):
        #code here
        def sort(arr):
            if len(arr)==1:
                return arr
            mid=len(arr)//2
            left=sort(arr[:mid])
            right=sort(arr[mid:])
            
            return self.merge(left,right)
            
        arr[:]=sort(arr)

#{ 
#  Driver Code Starts
#Initial Template for Python 3


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends