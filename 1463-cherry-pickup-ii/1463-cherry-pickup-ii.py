class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        c=len(grid[0])
        r=len(grid)
        dp={}
        
        for j1 in range(c):
            for j2 in range(c):
                if j1==j2:
                    dp[str([r-1,j1,j2])]=grid[r-1][j1]
                else:
                    dp[str([r-1,j1,j2])]=grid[r-1][j1]+grid[r-1][j2]
                    
        for i in range(r-2,-1,-1):
            for j1 in range(c-1,-1,-1):
                for j2 in range(c-1,-1,-1):
                    maxi=-1e8
                    for p in range(-1,2):
                        for q in range(-1,2):
                            val=0
                            if j1==j2:
                                val=grid[i][j1]
                            else:
                                val=grid[i][j1]+grid[i][j2]
                                
                            if (j1+p>=0 and j2+q>=0 and j1+p<c and j2+q<c):
                                val+=dp[str([i+1,j1+p,j2+q])]
                            else:
                                val+=-1e8
                            maxi=max(maxi,val)
                    dp[str([i,j1,j2])]=maxi
                    
        return dp[str([0,0,c-1])]