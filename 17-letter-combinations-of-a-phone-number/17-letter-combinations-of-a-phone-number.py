class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        arr=[]
        dict={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        length=len(digits)
        def f(ind,sak):
            if ind==len(digits):
                return ''
            for j in dict[digits[ind]]:
                sak+=j
                f(ind+1,sak)
                if len(sak)==length:
                    arr.append(sak)
                sak=sak[:-1]
        
        f(0,'')
        return arr