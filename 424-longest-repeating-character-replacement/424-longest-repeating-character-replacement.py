class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict={}
        ans=0
        
        l=0
        maxi=0
        for i in range(len(s)):
            try:
                dict[s[i]]+=1
            except:
                dict[s[i]]=1
            
            if (i-l+1)- max(dict.values())>k:
                dict[s[l]]-=1
                l+=1
                
            ans=max(ans,i+1-l)
        return ans
            