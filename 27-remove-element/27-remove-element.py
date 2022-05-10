class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i=0
        while(1):
            try:
                if nums[i]==-99:
                    break
                if nums[i]==val:
                    j=i
                    while(1):
                        try:
                            nums[j]=nums[j+1]
                            j+=1
                        except:
                            nums[j]=-99
                            break
                else:
                    i+=1
            except:
                break
        return i