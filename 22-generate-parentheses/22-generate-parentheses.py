class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        a=['(',')']
        arr=[]
        temp=''
        
        def f(open,close,temp):
            
            if open==n and close==n:
                arr.append(temp)
                
            elif open==n:
                temp+=')'
                f(open,close+1,temp)
            else:
                temp+='('
                f(open+1,close,temp)
                temp=temp[:-1]
                if open>close:
                    temp+=')'
                    f(open,close+1,temp)
        f(0,0,temp)
        return arr