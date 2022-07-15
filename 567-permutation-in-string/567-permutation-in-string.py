class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        else:
            orig={}
            for i in range(97,123):
                orig[chr(i)]=0    
            temp=orig.copy()

            for i in range(len(s1)):
                orig[s1[i]]+=1
                temp[s2[i]]+=1
            if temp==orig:
                return True
            else:
                i=0
                for j in range(len(s1),len(s2)):
                    temp[s2[j]]+=1
                    temp[s2[i]]-=1
                    i+=1
                    if orig==temp:
                        return True
                return False