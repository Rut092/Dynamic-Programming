class Solution:
	def wordLadderLength(self, startWord, targetWord, wordList):
		#Code here
		if startWord==targetWord:
		    return 0
		    
		if targetWord not in wordList:
		    return 0
		    
		abc={i:0 for i in wordList}
		
		que=[[startWord,1]]
		i=0
		while(i<len(que)):
		    
		    a,b=que[i]
		    i+=1
		    temp=[s for s in a]
		    
		    for j in range(len(startWord)):
		        
		        for m in range(ord('a'),ord('z')+1):
		            
		            temp[j]= chr(m)
		            l="".join(temp)
		            
		            if l in abc and l!=a:
		                que.append([l,b+1])
		                abc.pop(l)
		                
		            if l==targetWord:
		                return b+1
		                
		            temp[j]=a[j]
		
		return 0


#{ 
 # Driver Code Starts
from collections import deque 
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
		ans = obj.wordLadderLength(startWord, targetWord, wordList)
		print(ans)

# } Driver Code Ends