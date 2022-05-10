class Solution:
    def search(self, arr: List[int], target: int) -> int:
        
        def bin(min,max):
            
            while(min<=max):
                med=(min+max)//2
                
                if min==max:
                    if arr[min]==target:
                        return min
                    else:
                        return -1
                if min==max-1:
                    if arr[min]==target:
                        return min
                    elif arr[max]==target:
                        return max
                    else:
                        return -1
                if arr[med]==target:
                    return med
                elif target>arr[med]:
                    min=med
                else:
                    max=med
                
        
        def search(mal,map):
            mi=mal
            ma=map
            if mal==map:
                if arr[mal]==target:
                    return mal
                else:
                    return -1
            while(mi<ma):
                me=(mi+ma)//2
                if mi==ma-1:
                    if arr[mi]==target:
                        return mi
                    elif arr[ma]==target:
                        return ma
                    else:
                        return -1
                if arr[mi]<arr[me]:
                    a=bin(mi,me)
                    if a!=-1:
                        return a
                    mi=me
                elif arr[me]<arr[ma]:
                    a= bin(me,ma)
                    if a!=-1:
                        return a
                    ma=me
                    
        abc=-1 
        abc=search(0,len(arr)-1)
        if abc==None:
            return -1
        return abc
            