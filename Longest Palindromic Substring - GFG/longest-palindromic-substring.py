#User function Template for python3

class Solution:
    def longestPalindrome(self, S):
        # code here
        n=len(S)
        dp=[[0 for i in range(n)] for i in range(n)]
        il,fl=-1,-1
        cnt=1
        for i in range(n):
            dp[i][i]=1
            
        for i in range(n-1):
            if S[i]==S[i+1]:
                dp[i][i+1]=1
                if il==-1:
                    il,fl=i,i+1
        
        count=2
        for i in range(2,n):
            for j in range(0,n-count):
                if S[j]==S[j+count] and dp[j+1][j+count-1]==1:
                    dp[j][j+count]=1
                    if il==fl-1 or count!=cnt:
                        il,fl=j,j+count
                        cnt=count
            count+=1
        if il!=-1:
            return (S[il:fl+1])
        else:
            if il!=fl:
                return S[i:fl+1]
            else:
                return S[0:1]
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        S = input().strip()
        ob=Solution()
        print(ob.longestPalindrome(S))
# } Driver Code Ends