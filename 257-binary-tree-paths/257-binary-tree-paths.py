# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        arr=[]
        
        def f(root,temp):
            if root==None:
                return None
            
            temp.append(str(root.val))
            
            a=f(root.left,temp)
            b=f(root.right,temp)
            
            if a==None and b==None:
                arr.append(temp.copy())
            temp.pop(-1)
                
            return 1
            
            
        f(root,[])
        return ['->'.join(i) for i in arr]