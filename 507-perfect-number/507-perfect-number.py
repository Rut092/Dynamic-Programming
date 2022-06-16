import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        temp=1
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                temp+=i+num//i
        print(temp)
        if temp==num:
            if num==1:
                return False
            else:
                return True
        else:
            return False