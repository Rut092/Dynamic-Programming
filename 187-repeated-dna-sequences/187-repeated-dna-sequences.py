class Solution:
    def findRepeatedDnaSequences(self, a: str) -> List[str]:
        mini=[]
        dict={}
        n=len(a)
        for i in range(0,n-9):
            if (a[i:i+10]) not in dict:
                dict[a[i:i+10]]=1
            else:
                if dict[a[i:i+10]]==1:
                    mini.append(a[i:i+10])
                    dict[a[i:i+10]]+=1
        return mini