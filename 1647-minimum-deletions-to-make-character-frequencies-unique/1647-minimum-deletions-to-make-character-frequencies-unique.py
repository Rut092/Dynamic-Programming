class Solution:
    def minDeletions(self, s: str) -> int:
        dict={}
        ans=0
        for i in s:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        dict=[list(i) for i in sorted(dict.items(),key=lambda X:X[1],reverse=True)]
        val=[]
        for i in dict:
            if i[1] not in val:
                val.append(i[1])
            else:
                while(1):
                    if i[1]>0:
                        i[1]-=1
                        ans+=1
                        if i[1] not in val:
                            val.append(i[1])
                            break
                    else:
                        break
        return ans