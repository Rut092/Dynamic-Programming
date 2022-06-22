class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict={}
        length=0
        l=0
        for i in range(len(s)):
            try:
                if dict[s[i]]>=l:
                    l=dict[s[i]]+1
                    dict[s[i]]=i
                else:
                    dict[s[i]]=i
                    length=max(i-l+1,length)
            except:
                dict[s[i]]=i
                length=max(i-l+1,length)
        return length