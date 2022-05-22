class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map=[]
        value=[]
        for i in strs:
            a="".join(sorted(i))
            if a not in map:
                map.append(a)
                value.append([i])
            else:
                value[map.index(a)].append(i)
        return [sorted(i) for i in sorted(value,key=len)]