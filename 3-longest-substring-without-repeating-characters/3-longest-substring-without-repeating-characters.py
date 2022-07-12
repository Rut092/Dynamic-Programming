class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict={}
        for i in s:
            dict[i]=0
        
        i=0
        j=0
        l=len(s)
        ans=0
        temp=0
        while(l and j<l):
            if dict[s[j]]==0:
                temp+=1
                dict[s[j]]=1
                j+=1
                ans=max(ans,temp)
            else:
                dict[s[i]]=0
                temp-=1
                i+=1
            
        return ans