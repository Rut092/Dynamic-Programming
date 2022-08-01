class Solution:
    def canCross(self, stones: List[int]) -> bool:
        s=set(stones)
        @cache
        def f(val,prev):
            if val==prev:
                return False 
            if val==stones[-1]:
                return True
            if val in s:
                if f(val+(val-prev-1),val) or f(val+(val-prev),val) or f(val+(val-prev+1),val):
                    return True
        if stones[1]-stones[0]>1:
            return False
        return f(stones[1],stones[0])
        