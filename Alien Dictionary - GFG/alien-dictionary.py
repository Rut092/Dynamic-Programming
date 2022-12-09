#User function Template for python3

class Solution:
    def findOrder(self,dict, N, K):
    # code here
        a='abcdefghijklmnopqrstuvwxyz'
        alpha={}
        for i in range(K):
            alpha[a[i]]=i
        
        adj=[[] for i in range(K)]
        
        for i in range(N-1):
            for j in range(min(len(dict[i]),len(dict[i+1]))):
                if dict[i][j]!=dict[i+1][j]:
                    adj[alpha[dict[i][j]]].append(alpha[dict[i+1][j]])
                    break
        
        indeg=[0 for i in range(K)]
        
        for i in adj:
            for j in i:
                indeg[j]+=1
        
        q=[]
        arr=[]
        for i in range(K):
            if indeg[i]==0:
                q.append(i)
                arr.append(a[i])
                
        i=0
        while(i<len(q)):
            b=q[i]
            i+=1
            
            for p in adj[b]:
                indeg[p]-=1
                if indeg[p]==0:
                    q.append(p)
                    arr.append(a[p])
        
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends