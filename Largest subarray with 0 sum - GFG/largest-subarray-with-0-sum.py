#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        dict={}
        temp=0
        maxi=0
        for i in range(n):
            temp+=arr[i]
            if temp==0:
                maxi=i+1
            else:   
                try:
                    if maxi<i-dict[temp]:
                        maxi=i-dict[temp]
                    
                except:
                    dict[temp]=i
        return maxi
                
        
        
        
#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends