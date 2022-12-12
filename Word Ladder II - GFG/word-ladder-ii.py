#User function Template for python3

class Solution:
    def findSequences(self, startWord, targetWord, wordList):
        #Code here
        if startWord==targetWord:
		    return []
		    
		if targetWord not in wordList:
		    return []
		    
		abc={i:0 for i in wordList}
		
		que=[[startWord,1,[startWord]]]
		i=0
		
		deleting=set()
		sh=99
		val=0

		while(i<len(que)):
		    a,b,ans=que[i]
		    i+=1
		    temp=[s for s in a]
		    
		    
		    if b>val and len(deleting)!=0:
	            for x in deleting:
	                abc.pop(x)
	            deleting=set()
	            val=b
	            
	            
		    for j in range(len(startWord)):
		        
		        for m in range(ord('a'),ord('z')+1):
		            
		            temp[j]= chr(m)
		            l="".join(temp)
		            
		            if l in abc and l!=a:
		                if b<sh:
        		            que.append([l,b+1,ans+[l]])
		                deleting.add(l)
		                
		            temp[j]=a[j]
		            
		            if l==targetWord and sh==99:
		                sh=b+1
		            
		
		ans=[]
		
		for i in range(len(que)-1,-1,-1):
		    if que[i][1]==sh and que[i][2][-1]==targetWord:
		        ans.append(que[i][2])
		    if que[i][1]<sh:
		        break
		   
		return ans

#{ 
 # Driver Code Starts
from collections import deque 
import functools

def comp(a, b):
    x = ""
    y = ""
    for i in a:
        x += i 
    for i in b:
        y += i
    if x>y:
        return 1
    elif y>x:
        return -1 
    else:
        return 0

if __name__ == '__main__':
    T=int(input())
    for tt in range(T):
        n = int(input())
        wordList = []
        for i in range(n):
            wordList.append(input().strip())
        startWord = input().strip()
        targetWord = input().strip()
        obj = Solution()
        ans = obj.findSequences(startWord, targetWord, wordList)
        if len(ans)==0:
            print(-1)
        else:
            ans = sorted(ans, key=functools.cmp_to_key(comp))
            for i in range(len(ans)):
                for j in range(len(ans[i])):
                    print(ans[i][j],end=" ")
                print()

# } Driver Code Ends