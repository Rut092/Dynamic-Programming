# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        queue=[[root,1]]
        maxi=0
        while(queue):
            start=None
            n=len(queue)
            
            for i in range(len(queue)):
                
                node,val=queue.pop(0)

                if start==None:
                    start=val
                    
                if node.left!=None:
                    queue.append([node.left,2*val])  
                if node.right!=None:
                    queue.append([node.right,2*val+1])
                
                maxi=max(maxi,val-start+1)
            
        return maxi