class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        a=len(matrix[0])
        b=len(matrix)
        count=0
        
        for i in range(b):
            count+=matrix[i][0]
            
        for j in range(1,a):
            count+=matrix[0][j]

        for i in range(1,b):
            for j in range(1,a):
                
                if matrix[i][j]>0:
                    matrix[i][j]=min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])+1
                count+=matrix[i][j]

        return count