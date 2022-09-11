class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        a=len(matrix[0])
        b=len(matrix)
        count=0
        
        dp=matrix.copy()
        
        for i in range(b):
            dp[i][0]=matrix[i][0]
            count+=matrix[i][0]
            
        for j in range(1,a):
            dp[0][j]=matrix[0][j]
            count+=matrix[0][j]
            
        

        for i in range(1,b):
            for j in range(1,a):
                
                if matrix[i][j]>0:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                count+=dp[i][j]

        
     
        print(dp) 
        return count