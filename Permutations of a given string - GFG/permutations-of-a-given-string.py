#User function Template for python3

class Solution:
    def find_permutation(self, S):
        # Code here
        dict={}
        S=sorted(S)
        arr=[]
        for i in range(len(S)):
            dict[i]=0
        def f(s,temp):
            
            for i in range(len(s)):
                if dict[i]==0:
                    dict[i]=1
                    temp+=s[i]
                    a=f(s,temp)
                    temp=temp[:-1]
                    dict[i]=0
            
            if len(temp)==len(S):
                if temp not in arr:
                    arr.append(temp)
        
        f(S,'') 
        return arr


#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends