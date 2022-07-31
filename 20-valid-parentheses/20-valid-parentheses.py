class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        open={'(':')','[':']','{':'}'}
        
        for i in s:
            if i in open:
                stack.append(i)
            else:
                if len(stack)>0 and open[stack[-1]]==i:
                    stack.pop(-1)
                else:
                    return False
        if len(stack)>0:
            return False
        else:
            return True