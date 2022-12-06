#User function Template for python3

class Solution:
    def fill(self, n, m, mat):
        # code here
        
        res=[['X' for i in range(m)] for j in range(n)]
        
        que=[]
        
        for i in range(n):
            if mat[i][0]=='O':
                que.append([i,0])
                res[i][0]='O'
                mat[i][0]=''
                
            if mat[i][m-1]=='O':
                que.append([i,m-1])
                res[i][m-1]='O'
                mat[i][m-1]=''
                
        for i in range(m):
            if mat[0][i]=='O':
                que.append([0,i])
                res[0][i]='O'
                mat[0][i]=''
                
            if mat[n-1][i]=='O':
                que.append([n-1,i])
                res[n-1][i]='O'
                mat[n-1][i]=''
                
        
        i=0
        while(i<len(que)):
            a,b=que[i]
            i+=1
                
            if a>0 and mat[a-1][b]!="" and mat[a-1][b]=='O':
                    que.append([a-1,b])
                    res[a-1][b]='O'
                    mat[a-1][b]=""
                    
            if a<n-1 and mat[a+1][b]!="" and mat[a+1][b]=='O':
                    que.append([a+1,b])
                    res[a+1][b]='O'
                    mat[a+1][b]=""
                    
            if b>0 and mat[a][b-1]!="" and mat[a][b-1]=='O':
                    que.append([a,b-1])
                    res[a][b-1]='O'
                    mat[a][b-1]=""
            
            if b<m-1 and mat[a][b+1]!="" and mat[a][b+1]=='O':
                    que.append([a,b+1])
                    res[a][b+1]='O'
                    mat[a][b+1]=""
                    
        
        return res
            
                
            
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends