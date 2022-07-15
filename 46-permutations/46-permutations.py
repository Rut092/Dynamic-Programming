class Solution:
    def permute(self, S: List[int]) -> List[List[int]]:
        dict={}
        arr=[]
        for i in range(len(S)):
            dict[i]=0
        def f(s,temp):
            for i in range(len(S)):
                if dict[i]==0:
                    dict[i]=1
                    temp.append(S[i])
                    f(s,temp)
                    temp.pop(-1)
                    dict[i]=0
            if len(temp)==len(S):
                arr.append(temp.copy())
                
        f(S,[])
        return arr