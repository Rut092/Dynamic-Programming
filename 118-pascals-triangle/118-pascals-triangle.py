class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]
        
        for i in range(1,numRows):
            temp=[1]
            for j in range(1,len(ans[-1])):
                temp.append(ans[i-1][j-1]+ans[i-1][j])
            temp.append(1)
            ans.append(temp)
            
        return (ans)
            