class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs==[] or strs==[""]:
            return ""
        mini=len(strs[0])
        for i in strs:
            mini=min(mini,len(i))
        string=""
        for i in range(mini):
            for j in range(len(strs)):
                if j==0:
                    string+=strs[j][i]
                else:
                    if strs[j][i]!=string[-1]:
                        string=string[:-1]
                        return string
        return string
                    