class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        for i in range(len(triangle)-1,0,-1):
            for j in range(i):
                up=triangle[i-1][j]+triangle[i][j]
                di=triangle[i-1][j]+triangle[i][j+1]
                
                triangle[i-1][j]=min(up,di)
        return triangle[0][0]