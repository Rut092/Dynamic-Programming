class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        arr=sorted(boxTypes,key=lambda x:x[1],reverse=True)
        items=0
        i=0
        while(truckSize!=0):
            if i==len(arr):
                break
            a,b=arr[i]
            if truckSize-a>=0:
                items+=b*a
                truckSize-=a
            elif truckSize-a<0:
                items+=truckSize*b
                truckSize=0
                break
            i+=1
        return (items)