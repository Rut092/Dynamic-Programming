class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        a=len(matrix[0])
        b=len(matrix)
        dp=[[0 for i in range(a)] for j in range(b)]
        maxi=[0]
    
        def bfs(i,j,prev):
            if i<0 or i>=b or j<0 or j>=a:
                return 0
            elif dp[i][j]!=0 and matrix[i][j]>prev:
                return dp[i][j]
            else:
                if matrix[i][j]>prev:
                    m=1+bfs(i-1,j,matrix[i][j])
                    n=1+bfs(i+1,j,matrix[i][j])
                    o=1+bfs(i,j-1,matrix[i][j])
                    p=1+bfs(i,j+1,matrix[i][j])
                    dp[i][j]=max(m,n,o,p)
                    maxi[0]=max(maxi[0],dp[i][j])
                    
                    return dp[i][j]
                    
                else:
                    return 0

        for i in range(b):
            for j in range(a):
                bfs(i,j,-1)
        print(dp)
        return maxi[0]