class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        arr=[[-1]*len(grid[0])]*len(grid)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0 and j==0:
                    arr[i][j]=grid[0][0]
                else:
                    l=2**32
                    r=2**32
                    if i>0:
                        l=grid[i][j]+arr[i-1][j]
                    if j>0:
                        r=grid[i][j]+arr[i][j-1]
                    
                    arr[i][j]=min(l,r)
        return arr[-1][-1]