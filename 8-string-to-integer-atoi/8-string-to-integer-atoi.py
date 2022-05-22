class Solution:
    def myAtoi(self, s: str) -> int:
        arr=[]
        sign=[]
        for i in s:
            if i=='-' or i=='+':
                if arr==[]:
                    if len(sign)>0:
                        arr=[]
                        return 0
                    else:
                        sign.append(i)
                else:
                    break
            else:
                try:
                    int(i)
                    arr.append(i)
                except:
                    if i==" " and len(arr)>0:
                        break
                    if i==" " and len(sign)>0:
                        break
                    elif i!=' ':
                        break
                    
        if arr==[]:
            return 0
        if len(sign)>0:
            if sign[0]=='-':
                if int('-'+''.join(arr))<=-2147483648:
                    return -2147483648
                else:
                    return int('-'+''.join(arr))
            else:
                if int(''.join(arr))>=(2**31-1):
                    return (2**31-1)
                else:
                    return int(''.join(arr))
                
        else:
            if int(''.join(arr))>=(2**31-1):
                return (2**31-1)
            else:
                return int(''.join(arr))
            