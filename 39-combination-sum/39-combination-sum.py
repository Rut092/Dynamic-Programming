class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        arr=[]
        def f(ind,arr,target):
            if target==0:
                ans.append(arr.copy())
                
            elif ind==len(candidates):
                return
            
            else:
                if candidates[ind]<=target:
                    arr.append(candidates[ind])
                    pick=f(ind,arr,target-candidates[ind])
                    arr.pop(-1)
                not_pick=f(ind+1,arr,target)
         
        f(0,arr,target)
        return ans
                