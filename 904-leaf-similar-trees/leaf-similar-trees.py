# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,arr):
        if not root:
            return
        if root.left==None and root.right==None:
            arr.append(root.val)
        self.inorder(root.left,arr)
        self.inorder(root.right,arr)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        ans1=[]
        ans2=[]
        self.inorder(root1,ans1)
        self.inorder(root2,ans2)
        return ans1==ans2