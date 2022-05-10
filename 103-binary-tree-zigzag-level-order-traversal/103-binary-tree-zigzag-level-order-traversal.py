# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stk1=[]
        stk2=[]
        ans=[]
        if root!=None:
            stk2.append(root)
            ans.append([root.val])
            dir=1
            while(1):
                if dir==0:
                    if len(stk1)==0:
                        break
                    stk1=(stk1)[::-1]
                    abc=[]
                    for i in stk1:
                        if i.left!=None:
                            stk2.append(i.left)
                            abc.append(i.left.val)
                        if i.right!=None:
                            stk2.append(i.right)
                            abc.append(i.right.val)
                    if len(abc)!=0:
                        ans.append(abc)
                    abc=[]                
                    stk1=[]

                elif dir==1:
                    if len(stk2)==0:
                        break
                    stk2=(stk2)[::-1]
                    abc=[]
                    for i in stk2:
                        if i.right!=None:
                            stk1.append(i.right)
                            abc.append(i.right.val)
                        if i.left!=None:
                            stk1.append(i.left)
                            abc.append(i.left.val)
                    if len(abc)!=0:
                        ans.append(abc)
                    abc=[]
                    stk2=[]
                if dir==0:
                    dir=1
                elif dir==1:
                    dir=0
            else:
                return []
        return (ans)

                        