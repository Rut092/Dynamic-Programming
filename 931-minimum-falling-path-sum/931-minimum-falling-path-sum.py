class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        a=len(matrix)
        
        for i in range(a-2,-1,-1):
            for j in range(a-1,-1,-1):
                b1=2**32
                b3=2**32
                b2=matrix[i][j]+matrix[i+1][j]
                if j>0:
                    b1=matrix[i][j]+matrix[i+1][j-1]
                if j<a-1:
                    b3=matrix[i][j]+matrix[i+1][j+1]
                    
                matrix[i][j]=min(b1,b2,b3) 
                
        return (min(matrix[0]))