class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        a=len(matrix[0])
        b=len(matrix)
        count=0
        for i in range(b):
            for j in range(a):
                if i>0 and j>0 and matrix[i][j]>0:
                    matrix[i][j]=min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])+1
                count+=matrix[i][j]

        return count