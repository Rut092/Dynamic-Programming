class Solution:
    def findRepeatedDnaSequences(self, a: str) -> List[str]:
        mini=[]
        dict={}
        n=len(a)
        for i in range(0,n-9):
            try:
                if dict[a[i:i+10]]==1:
                    mini.append(a[i:i+10])
                    dict[a[i:i+10]]+=1
            except:
                dict[a[i:i+10]]=1
        return mini