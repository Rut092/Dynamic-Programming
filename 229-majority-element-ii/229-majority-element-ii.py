class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1=-1
        num2=-1
        c1=0
        c2=0
        for i in nums:
            if num1==i:
                c1+=1
            elif num2==i:
                c2+=1
            elif c1==0:
                num1=i
                c1+=1
            elif c2==0:
                num2=i
                c2+=1
            else:
                c1-=1
                c2-=1
        count1=0
        count2=0
        for i in nums:
            if i==num1:
                count1+=1
            elif i==num2:
                count2+=1
        a=1
        b=1
        if count1>len(nums)/3:
            a=0
        if count2>len(nums)/3:
            b=0
        if a==b:
            if a==1:
                return []
            elif a==0:
                return [num1,num2]
        else:
            if b==0:
                return [num2]
            else:
                return [num1]