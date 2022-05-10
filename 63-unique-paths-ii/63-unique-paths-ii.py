class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                
                if obstacleGrid[i][j]==1:
                    obstacleGrid[i][j]=0
                elif i==0 and j==0:
                    obstacleGrid[0][0]=1
                else:
                    dn=0
                    rt=0
                    
                    if i>0:
                        dn=obstacleGrid[i-1][j]
                    if j>0:
                        rt=obstacleGrid[i][j-1]
                        
                    obstacleGrid[i][j]=dn+rt
        return obstacleGrid[-1][-1]