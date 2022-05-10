# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr=[]
        
        
        def pre(root,level,wid):
            if root==None:
                return
            arr.append([root.val,level,wid])
            pre(root.left,level+1,wid-1)
            pre(root.right,level+1,wid+1)
        
        pre(root,0,0)
        arr=sorted(sorted(arr,key=lambda x:x[0]),key=lambda x:x[1])
        arr=sorted(arr,key=lambda x:x[2])
        sec={}
        for i in arr:
            a,b,c=i
            if c in sec:
                sec[c].append(a)
            else:
                sec[c]=[a]
        return (list(sec.values()))