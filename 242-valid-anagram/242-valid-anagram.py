class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict={}
        for i in s:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        
        for i in t:
            try:
                dict[i]-=1
            except:
                return False
        
        for i in dict:
            if dict[i]!=0:
                return False
        
        return True
        
        